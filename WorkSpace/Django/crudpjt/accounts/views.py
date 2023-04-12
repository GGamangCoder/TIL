from django.shortcuts import render, redirect
# 인증과 권한 모델(폼)
from django.contrib.auth.forms import AuthenticationForm
# 로그인 / 로그아웃
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 회원가입 / 탈퇴
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
# 로그인 / 로그아웃
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# 회원 가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)