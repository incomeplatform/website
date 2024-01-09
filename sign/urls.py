from django.urls import path
from . import views

urlpatterns = [
    # User Registration
    path('api/register/', views.api_register_user, name='api_register_user'),
    path('register/', views.register_user, name='register_user'),

    # User Sign-In
    path('api/login/', views.api_login_user, name='api_login_user'),
    path('login1/', views.login_user, name='login_user'),

    # Password Reset
    path('api/reset_password/', views.api_reset_password, name='api_reset_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
