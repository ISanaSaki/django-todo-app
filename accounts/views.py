from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm, UserLoginForm


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password'],
                first_name=cd['firstname'],
                last_name=cd['lastname'],
            )
            messages.success(request, 'user created successfully!', 'success')
            return redirect('login_user')
    else:
        form = UserCreateForm()
    return render(request, 'user_create.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully!', 'success')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'logged out successfully!', 'success')
    return redirect('home')
