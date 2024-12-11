from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from users.models import User
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('users:profile'))
        else:
            return render(request, 'users/users.html')
    return render(request, 'users/users.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        auth_login(request, user)
        return redirect('users:profile')
    
    return redirect('users:login')


def profile(request):
    return render(request, 'users/profile.html')


def logout(request):
    auth_logout(request)
    return redirect('users:login')