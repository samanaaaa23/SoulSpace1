from django.db import models
from django.contrib.auth.models import User
import random
import string
# Create your models here.

#utility function to generate OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

class UserOtherDetails(models.Model): #custom model for storing additional info about users
    TYPE_CHOICES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='other_details') #one to one relationship with django's default user model
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True) #handles opt storage and verification status
    otp_created_at = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='basic')  # 🡄 new field added

    def generate_new_otp(self):
        self.otp = generate_otp()
        self.otp_created_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Other Details"