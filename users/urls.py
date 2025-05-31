from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    UserView,
    VerifyOTPView,
    ChangePasswordView,
    update_user_details,
    update_user_type,
    khalti_lookup_user_type,  # 👈 Add this import
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update_user_details/', update_user_details, name='update_user_details'),
    path('update-user-type/', update_user_type, name='update-user-type'), 
    path('khalti-lookup-user-type/', khalti_lookup_user_type, name='khalti-lookup-user-type'),  # 👈 NEW
]
