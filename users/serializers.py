from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserOtherDetails
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
import string
class UserOtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOtherDetails
        fields = ['phone_number', 'address', 'date_of_birth', 'profile_picture','type']
class UserSerializer(serializers.ModelSerializer):
    other_details = UserOtherDetailsSerializer(read_only=True)  # Add the related user details here
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'other_details','date_joined','is_superuser']

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        # Generate OTP
        otp = generate_otp()

        # Create UserOtherDetails entry with OTP
        UserOtherDetails.objects.create(
            user=user,
            otp=otp,
            otp_created_at=timezone.now()
        )

        # Send OTP via email with HTML template
        subject = 'Your OTP Code'
        html_message = render_to_string('otp/otp_email_template.html', {'otp': otp, 'user': user})
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            'no-reply@yourdomain.com',
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )

        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


class OTPVerificationSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        otp = data['otp']
        user = self.context['request'].user 

        try:
            user_details = user.other_details  
        except UserOtherDetails.DoesNotExist:
            raise serializers.ValidationError("User details not found.")

        if user_details.otp != otp:
            raise serializers.ValidationError("Invalid OTP.")

       
        user_details.otp = ''
        user_details.is_verified = True
        user_details.save()

      
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }
