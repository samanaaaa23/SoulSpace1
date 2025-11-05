from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Category, Author, Course, Lesson, SubCategory, Order
from .serializers import CategorySerializer,OrderSerializer, AuthorSerializer, CourseSerializer, LessonSerializer,SubCategorySerializer,CategoryWithCoursesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.conf import settings
import uuid, json, requests
from rest_framework.permissions import AllowAny, IsAuthenticated
# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

# Author ViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Lesson ViewSet
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().select_related('category')  # Efficiently fetch related category data
    serializer_class = SubCategorySerializer

class CategoryWithCoursesView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # Fetch the category along with subcategories and courses
            category = Category.objects.prefetch_related('subcategories', 'courses').get(id=pk)

            # Serialize the data
            serializer = CategoryWithCoursesSerializer(category)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        


@api_view(['POST'])

def create_order(request):
    serializer = OrderSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid():
        order = serializer.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def initiate_khalti_payment(request):
    try:
        data = request.data
        course_title = data.get("course_title", "Course Payment")
        price = 10000  
        course_id = data.get("course_id")
        session_id = data.get("session_id")  
        user = request.user

        appointment_id = str(uuid.uuid4())

        #  Create a "Pending" order (now include 'user')
        order_data = {
            "user": user.id,  # 👈 Add this line!
            "course_title": course_title,
            "course_id": course_id,
            "price": price / 100,
        }
        print("Creating Pending Order with data:", order_data)

        serializer = OrderSerializer(data=order_data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=400)

        payload = json.dumps({
            "return_url": "http://localhost:3000/userdashboard/usersessions",
            "website_url": "http://localhost:3000/userdashboard/usersessions",
            "amount": int(price),
            "purchase_order_id": appointment_id,
            "purchase_order_name": course_title,
        })

        headers = {
            'Authorization': 'key 88f2d8f1bf1c4b78b7b518371e887c7b',
            'Content-Type': 'application/json',
        }

        response = requests.post("https://dev.khalti.com/api/v2/epayment/initiate/", headers=headers, data=payload)
        rep = response.json() if response.content else None

        if response.status_code == 200 and rep:
            return Response({ "payment_url": rep['payment_url'] }, status=200)
        else:
            return Response({ "error": rep or "Khalti error" }, status=400)

    except Exception as e:
        return Response({ "error": str(e) }, status=500)

    
@api_view(["GET"])
def khalti_lookup(request):
    print("Khalti lookup view called with parameters:", request.GET)

    try:
        pidx = request.GET.get("pidx")
        course_id = request.GET.get("course_id")
        session_id = request.GET.get("session_id")

        if not course_id or not pidx:
            return Response({"error": "Missing required parameters."}, status=400)

        headers = {
            'Authorization': 'key 638d4c0a1d2b4f1d94430254e6683d35',
            'Content-Type': 'application/json',
        }

        response = requests.post(
            "https://dev.khalti.com/api/v2/epayment/lookup/",
            headers=headers,
            data=json.dumps({ "pidx": pidx })
        )

        if not response.content:
            return Response({"error": "Empty response from Khalti on lookup"}, status=500)

        rep = response.json()

        if rep.get('status') == "Completed":
           

            # Prepare order data
            order_data = {
                "course": course_id,
                "user": request.user.id,
                "transaction_id": pidx,
                "amount": rep.get("total_amount", 0) / 100,
                "status": "Confirmed",
            }

            order_serializer = OrderSerializer(data=order_data, context={'request': request})
            if order_serializer.is_valid():
                order = order_serializer.save()
                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
            else:
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "Payment status is not completed."}, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
@api_view(["GET"])
@permission_classes([IsAuthenticated]) 
def user_orders(request):
    user = request.user  
    orders = Order.objects.filter(user_id=user.id).order_by('-created_at')  
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)



    
