# app_name/admin.py

from django.contrib import admin
from .models import CustomUser  # Import the CustomUser model

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'school_or_college')  # Update list_display
    search_fields = ('username', 'email')
    list_filter = ('school_or_college',)  # Update list_filter
