from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


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
    pass