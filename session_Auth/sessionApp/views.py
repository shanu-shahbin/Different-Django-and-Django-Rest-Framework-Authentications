from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  

def account(request):
    return render(request, 'account.html')

@login_required
def home(request):
    if request.session.get_expiry_age() <= 0:
        # Check if session has expired
        return redirect('login')
    else:
        # Session has not expired, render the home page
        return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('home')
        else:
            # Return an error message
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
       
        login(request, user)
        # Redirect to a success page or homepage
        return redirect('login')
    else:
    
        return render(request, 'register.html')  

def logout_view(request):
    logout(request)
    # Redirect to a success page or homepage
    return redirect('account')
