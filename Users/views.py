from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import CustomUserCreationForm
from django.shortcuts import render, redirect


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

    return render(request, 'Users/regiester.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'Users/login.html')


@login_required
def logout_view(request):
    # Capture the referring URL
    next_url = request.META.get('HTTP_REFERER', 'home')

    logout(request)

    return redirect(next_url)
