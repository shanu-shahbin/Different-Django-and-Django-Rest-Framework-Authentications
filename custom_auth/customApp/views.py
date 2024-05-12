from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm  # Import your user registration form if you have one
from .models import User  # Import your custom user model

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Custom authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('success_url')
        else:
            # Return an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def success_view(request):
    return HttpResponse("Login Successful!")

def account(request):
    # Placeholder view for account page
    return render(request, 'account.html')

def home(request):
    # Placeholder view for home page
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
