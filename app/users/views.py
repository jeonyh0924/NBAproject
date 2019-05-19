from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.models import User
from .forms import LoginForm, SignupForm


# Create your views here.
def login_view(request):
    # URL : /users/login/
    # config.urls 에서 '/users/' 부분을 'users.urls'를 사용하도록 include
    # users.urls에서 '/login/' 부분을 이 view 에 연결
    #
    # Template: /users/login.html
    # 템플릿의 get 요청 시 아래의 loginForm 인스턴스를 사용
    # posts 요청 시 처리는 아직 하지 않는다.

    if request.method == 'POST':
        # 1. requset.POST에 데이터가 옴
        # 2. 온 데이터 중에서 username에 해당하는 값과 password에 해당하는 값을 각각
        # 사용자 인증을 수행한다.
        # 3. 사용자 인증을 수행
        #   username / password 에 해당하는 사용자가 있는지 확인
        # 4-1. 인증에 성공하면
        #   세션 쿠키 기반의 로그인 과정을 수행, 완료 후 posts:post-list 페이지로 Redirect
        # 4-2. 인증에 실패한다면,
        #   이 페이지에서 인증이 실패 하였음을 사용자에게 알려준다.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            # 인증 실패
            pass
    else:
        form = LoginForm()
        context = {
            'form': form,

        }
        return render(request, 'users/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')


def signup_view(request):
    # URL : /users/signup/
    # templates : users/signup.html
    # form
    #   SignupForm
    #       username, password, password2
    #   나머지 요소들은 login.html의 요소를 최대한 활용

    # GET 요청 시 해당 템플릿 보여주도록 처리
    # base.html 에 있는 'SignUp' 버튼이 이 쪽으로
    # 이동할 수 있도록 url 링크 걸기
    context = {
        'form': SignupForm(),
    }
    # 1. request.post에 전달이 된 username, password1, password2를
    # 각각의 변수 에 할당
    # 2-x 에서는 httpresponse 에 문자열로 에러를 리턴해주기
    # 2-1. username 에 해당하는 User가 이미 있다면
    #       username 은 이미 사용중
    # 2-2. password1 과 2가 일치하지 않다면
    #  비밀번호 확인란 에러
    # 3. 위의 두 경우가 아니라면
    #  새 유저를 생성
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        introduce = request.POST['introduce']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if User.objects.filter(username=username).exists():
            context['error'] = f'사용자명({username})은 이미 사용중입니다.'
        elif password1 != password2:
            context['error'] = '비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다'
        else:
            # create_user메서드는 create와 달리 자동으로 password해싱을 해줌
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                introduce=introduce,
                first_name=first_name,
                last_name=last_name,
            )
            login(request, user)
            return redirect('posts:post-list')
    return render(request, 'users/signup.html', context)

