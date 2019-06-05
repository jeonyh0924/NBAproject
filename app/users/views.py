import imghdr
import io
import json
from pprint import pprint

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.models import User
from .forms import LoginForm, SignupForm, UserProfileForm

User = get_user_model()


# Create your views here.
def login_view(request):
    # URL : /users/login/
    # config.urls 에서 '/users/' 부분을 'users.urls'를 사용하도록 include
    # users.urls에서 '/login/' 부분을 이 view 에 연결
    #
    # Template: /users/login.html
    # 템플릿의 get 요청 시 아래의 loginForm 인스턴스를 사용
    # posts 요청 시 처리는 아직 하지 않는다.
    context = {}
    if request.method == 'POST':

        # username, password 를 받는 부분을
        # LoginForm 을 사용하도록 수정
        # 로그인에 실패를 하였을 경우, Template의 field에 form.non_field_errors를 사용해서
        # 로그인에 실패를 하였음을 출력

        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            # get 파라미터에 'next'가 전달되면
            # 해당 키의 값으로 Redirect
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            # 전달이 되지 않았으면, 'posts:post-list'로 redirect
            return redirect('posts:post-list')
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')


def signup_view(request):
    context = {}
    if request.method == 'POST':
        # POST 로 전달 된 데이터를 확인
        # 올바르다면 User를 생성하고, post-list로 이동
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post-list')
    else:
        form = SignupForm()

    context['form'] = form
    # GET 요청 시 또는 POST로 전달된 데이터가 올바르지 않을 경우
    # signup.html에
    # 빈 form 또는 올바르지 않은 데이터에 대한 정보가 포함 된 form을 전달해서 동적으로 form 렌더
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필의 수정이 완료 되었습니다.')
    form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'users/profile.html', context)


def facebook_login(request):
    user = authenticate(request, facebook_request_token=request.GET.get('code'))
    if user:
        login(request, user)
        return redirect('posts:post-list')
    messages.error(request, '페이스북 로그인에 실패를 하였습니다.')
    return redirect('users:login')
