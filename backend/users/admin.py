# users/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Register UserProfile in the admin panel
admin.site.register(UserProfile)
