# app_name/views.py
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUser, ResetPasswordSerializer
from django.contrib.auth.views import LoginView
from django.contrib import messages

# API view for user registration
@api_view(['POST'])
def api_register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        phone = request.data.get('phone')
        school_or_college = request.data.get('school_or_college')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        errors = {}
        if len(username) < 1:
            errors['username'] = 'Username is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if len(phone) < 10 or len(phone) > 14:
            errors['phone'] = 'Phone must be between 10 and 14 digits.'
        if len(password) != 6:
            errors['password'] = 'Password must be 6 digits long.'
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({'errors': {'email': 'Email already exists.'}}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)
        user = CustomUser(username=username, email=email, phone=phone, school_or_college=school_or_college, password=hashed_password)
        user.save()

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

# API view for user login
@api_view(['POST'])
def api_login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'login': 'Invalid credentials'}}, status=status.HTTP_401_UNAUTHORIZED)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('stuprofile:profile')
        else:
            return render(request, 'login_user.html', {'error': 'Invalid username or password'})

    return render(request, 'login_user.html')

# API view for resetting user password
@api_view(['POST'])
def api_reset_password(request):
    if request.method == 'POST':
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            new_password = serializer.validated_data['new_password']

            user = CustomUser.objects.filter(username=username, email=email, phone=phone).first()
            if user:
                user.password = make_password(new_password)
                user.save()
                return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'reset_password': 'Invalid user information'}}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Template view for user registration
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        school_or_college = request.POST.get('school_or_college')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        errors = {}
        if len(username) < 1:
            errors['username'] = 'Username is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if len(phone) < 10 or len(phone) > 14:
            errors['phone'] = 'Phone must be between 10 and 14 digits.'
        if len(password) < 5:
            errors['password'] = 'Password must be 6 digits long.'
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        if errors:
            return render(request, 'register_user.html', {'errors': errors})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register_user.html', {'errors': {'email': 'Email already exists.'}})

        hashed_password = make_password(password)
        user = CustomUser(username=username, email=email, phone=phone, school_or_college=school_or_college, password=hashed_password)
        user.save()

        return JsonResponse({'message': 'User registered successfully'})

    else:
        return render(request, 'register_user.html')

# Template view for resetting user password
def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new_password = request.POST.get('new_password')

        errors = {}
        if len(username) < 1:
            errors['username'] = 'Username is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if len(phone) < 10 or len(phone) > 14:
            errors['phone'] = 'Phone must be between 10 and 14 digits.'
        if len(new_password) < 5:
            errors['new_password'] = 'New password must be 6 digits long.'

        if errors:
            return render(request, 'reset_password.html', {'errors': errors})

        user = CustomUser.objects.filter(username=username, email=email, phone=phone).first()
        if user:
            user.password = make_password(new_password)
            user.save()
            return JsonResponse({'message': 'Password reset successfully'})
        else:
            return render(request, 'reset_password.html', {'errors': {'reset_password': 'Invalid user information'}})
    else:
        return render(request, 'reset_password.html')
