from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view, permission_classes
from .models import UserOtherDetails
import uuid
import json
import requests
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    OTPVerificationSerializer
)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT Tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)


class VerifyOTPView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response({"detail": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(new_password, user)
        except Exception as e:
            return Response({"detail": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password updated successfully."})
    
@api_view(['PUT'])
def update_user_details(request):
    user = request.user  # Get the authenticated user from the request
    
    # Retrieve data from request
    username = request.data.get("username")
    email = request.data.get("email")
    
    # Ensure that both username and email are provided
    if not username or not email:
        return Response({"detail": "Username and email are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Update Auth User details (username, email)
    user.username = username
    user.email = email
    user.save()

    # Now update UserOtherDetails
    phone_number = request.data.get("phone_number")
    address = request.data.get("address")
    date_of_birth = request.data.get("date_of_birth")
    
    # Use get_or_create to handle case where the UserOtherDetails object doesn't exist
    user_other_details, created = UserOtherDetails.objects.get_or_create(user=user)
    
    user_other_details.phone_number = phone_number
    user_other_details.address = address
    user_other_details.date_of_birth = date_of_birth
    
    # Handle profile picture if provided
    profile_picture = request.FILES.get('profile_picture')
    if profile_picture:
        user_other_details.profile_picture = profile_picture
    
    user_other_details.save()

    return Response({"message": "Profile updated successfully!"}, status=status.HTTP_200_OK)




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_user_type(request):
    """
    Initiate Khalti payment for upgrading user type.
    """
    try:
        data = request.data

        new_type = data.get("type")  # "basic" or "premium"
        
        if new_type not in ['basic', 'premium']:
            return Response({"error": "Invalid type. Must be 'basic' or 'premium'."}, status=400)

        user = request.user

        if not hasattr(user, 'other_details'):
            return Response({"error": "UserOtherDetails not found for this user."}, status=404)

     
        user_other_details = user.other_details
        user_other_details.type = new_type
        user_other_details.save()


        appointment_id = str(uuid.uuid4())

        price_in_rupees = 1000 if new_type == 'premium' else 500

        payload = json.dumps({
            "return_url": f"http://localhost:3000/userdashboard/membership",
            "website_url": "http://localhost:3000/userdashboard/membership",
            "amount": int(price_in_rupees * 100),  # Khalti uses paisa
            "purchase_order_id": appointment_id,
            "purchase_order_name": f"{user.username} {new_type} Membership",
        })

        headers = {
            'Authorization': 'key 88f2d8f1bf1c4b78b7b518371e887c7b',
            'Content-Type': 'application/json',
        }

        response = requests.post("https://dev.khalti.com/api/v2/epayment/initiate/", headers=headers, data=payload)
        rep = response.json() if response.content else None

        if response.status_code == 200 and rep:
            return Response({
                "message": f"Initiated payment for '{new_type}' membership.",
                "payment_url": rep['payment_url']
            }, status=200)
        else:
            return Response({
                "error": rep or "Failed to initiate Khalti payment."
            }, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def khalti_lookup_user_type(request):
    """
    Look up payment status from Khalti and update user type if successful.
    """
    try:
        pidx = request.GET.get("pidx")
        membership_type = request.GET.get("type")

        if not pidx or not membership_type:
            return Response({"error": "Missing required parameters: 'pidx' and 'type'."}, status=400)

        if membership_type not in dict(UserOtherDetails.TYPE_CHOICES):
            return Response({"error": "Invalid membership type."}, status=400)

        headers = {
            'Authorization': 'key 88f2d8f1bf1c4b78b7b518371e887c7b',
            'Content-Type': 'application/json',
        }

        lookup_response = requests.post(
            "https://dev.khalti.com/api/v2/epayment/lookup/",
            headers=headers,
            data=json.dumps({ "pidx": pidx })
        )

        if not lookup_response.content:
            return Response({"error": "Empty response from Khalti on lookup."}, status=500)

        result = lookup_response.json()

        if result.get("status") != "Completed":
            return Response({"error": f"Payment not completed. Status: {result.get('status')}"}, status=400)

        user = request.user
        user_other_details = getattr(user, 'other_details', None)
        if not user_other_details:
            return Response({"error": "UserOtherDetails not found for user."}, status=404)

        user_other_details.type = membership_type
        user_other_details.save()

        return Response({
            "message": f"Membership upgraded to '{membership_type}' successfully.",
            "transaction_id": pidx,
        }, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)

