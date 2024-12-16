# users/urls.py

from django.urls import path
from .views import (
    login_view,
    logout_login_view,
    logout_view,
    register_view,
    handle_signup,
    handle_login,
    index_view,
    profile,
    
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login/', logout_login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("handleSignup/", handle_signup,name="handleSignup"), # Add this line
    path('handlelogin/', handle_login, name='handlelogin'),
    path('', index_view, name='index'),
    path('register/', register_view, name='register'),
    path('profile/', profile, name='profile'),
]
