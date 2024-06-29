from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def regiester(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(
                request, 'Registration failed. Please correct the error below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'regiester.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
