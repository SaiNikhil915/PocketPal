# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from transactions.models import Transaction
from django.contrib.auth.decorators import login_required


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with your URL pattern name for index.html
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

# Register View
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "User successfully registered")
            return redirect('login')

    return render(request, 'users/register.html')

def handle_signup(request):
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        profession = request.POST['profession']
        income = request.POST['income']
        savings = request.POST['Savings']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for password confirmation error
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Create the user
        try:
            user = User.objects.create_user(username=uname, email=email, password=pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()

            # Show success message
            messages.success(request, "Account created successfully! Please login.")
            
            # Redirect to login page
            return redirect("login")

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect("register")
    else:
        return redirect("register")


def handle_login(request):
    if request.method == "POST":
        try:
            username = request.POST['loginuname']  # Correct key to access the username input
            password = request.POST['loginpassword1']  # Correct key to access the password input
        except KeyError:
            return render(request, 'users/login.html', {'error': 'Both fields are required.'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index page after login
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return redirect('login')  # Redirect if the method is not POST
  # Redirect to login for non-POST methods



def logout_view(request):
    logout(request)  # Logs out the user
    return render(request, 'users/logout.html')


def index_view(request):
    return render(request, 'dashboard/index.html')  

def logout_login_view(request):
    return render(request, 'users/login.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')  # Render the profile template