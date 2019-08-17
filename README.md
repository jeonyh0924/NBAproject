# NBA develop

## Installation

###Requirements
- python 3.6
- Django 2.1

pip

###secrets 

'secrets/base.json'

```
json
{
	"SECRET_KEY":"<Django secret key>"
	"FACEBOOK_APP_ID":<Facebook app id>,
	"FACEBOOK_APP_SECRET":"<Facebook app Secret>"
}

```

#### 6월 중순에 학기가 끝나고 readme에 정리한 내용들을 깃 블로그에 정리해서 올릴 것 입니다. 

[정규표현식](https://highcode.tistory.com/6)

[모델링 정방향 역방향] (https://whatisthenext.tistory.com/118)
## settings.py
STATICFILES_DIRS = [
    STATIC_DIR,
]
1. 개발 모드에서 settings.STATIC_URL 에 해당하는 request는
2. settings.STATICFILES_DIRS 리스트 내의 경로목록 각각의 하위 위치에서 해당 파일을 검색하며 존재한다면 그 파일을 리턴해준다. 

### 크롤링 사이트 참고 - 파일 경로 설정

[파일경로설정](https://thispointer.com/how-to-create-a-directory-in-python/)
### 셀리니움 
[셀레니움](https://selenium-python.readthedocs.io/locating-elements.html)


###s3 시행착오
> 문제점 : 크롤링을 한 이미지 파일을 s3에 업로드 한 뒤, 장고와 
> 연결하여 파일업로드를 동적으로 처리하고 싶었으나 
> No such key로 존재하지 않는 파일로 인식하며 연결이 이루어지지 않았다.

>이미지 필드에 택스트로 정리한 것이 문제였다. f'{}

>이를 해결 할 수 있었던 기능을 가진 속성은 upload_to

>이것은 동적으로 path를 주었다.

>텍스트로 저장을 하였을때에는 이미지가 저장이 되지 않고 경로만 저장이 되었다. 
이를 해결한 방법은 이미지를 다운받고, 메모리에 바이너리로 오픈하고 인스턴스를 생성할 때, 오픈된 바이너리 데이터를 보내주었다. 
이를 하게 되면 이미지는 실제로 바이너리 파일로 저장이 되고, 경로는 upload_to에 의해 자동으로 저장이 되었다. 



## NamedTuple 나중에 써서 분리해보기 

크롤링 코드 각 모델별로 분리해서 모델 매니저를 통해서 관리 .


## django admin 커스터마이징
[박영우 님의 파이콘 한국 2017 발표자료]
(https://www.slideshare.net/bbayoung7849/djangoadminsitecustomexample)

[장고 어드민 스타일링]
(https://teamlab.github.io/jekyllDecent/blog/tutorials/Django-Admin-%EC%BB%A4%EC%8A%A4%ED%84%B0%EB%A7%88%EC%9D%B4%EC%A7%95)


* settings에서 installed_apps = {
	'<modulename>.apps.<Modulename>Config'
	하고
	apps에서 verbose_name으로 관리자페이지에서 바꾸고 싶은 이름으로 지정하면 모델 이름도 바뀐다. settings.py에 installed_apps 에 저렇게 경로를 지정해 주는 것은 장고에서 권장하는 방식이다.
	
* models.py에서 모델클래스에 
class Meta:
	verbose_name = '지정 이름'
	verbose_name_plurla = f'{verbose_name} 목록'
으로 하면 

## django modeling 정리
* Foreignkey (on_delete = model.CASECADE)
>모델 A와 모델 B가 M:1 관계일 때, 모델 A에 on_delete = model.CASECADE가 설정되어 있으면, 모델 B의 어떤 레코드가 삭제되면 삭제될 모델 B의 레코드와 관련된 모델 A의 레코드도 삭제된다. 

>즉 지워질 때, 같이 지워지게 종속관계를 설정하는 것, 
>선수 모델이 팀 모델에 외래키를 걸고 CASECADE 설정을 하게 되면
>선수 모델이 제거될 때 팀 모델 또한 삭제된다. 

* 모델 간에 관계를 맺을 시 참고사항

> ex) .Foreignkey("User") ""을 사용하면 존재하지 않는 클래스에 대해서 나중에 생성을 할 테니 오류표시를 하지 말라는 표시가 된다. 
이는 클래스의 생성에서 관계에 대한 우선 순위를 고려하지 않아도 되어 개발에 용이한 것 같다. 

> 다른 모듈에 있는 클래스를 참조할 시에 '<AppName>.<modelName>' 을 하면 어떠한 모듈의 모델을 참조하는지 명시적으로 표시 할 수 있다. ''를 달지 않으면 command를 통해서 바로 해당하는 모델로 들어 갈 수 있지만 ''을 달게 되면 텍스트가 되므로 appname을 달아주어서 명시적으로 표시하는 것이 개발시 도움이 될 것 같다. 

* Null 과 blank 차이 

> 필드를 비워둘 것인지 허용하는 방법
> Null = True 필드의 값이 Null ( 정보 없음 ) 으로 저장되는 것을 허용한다. null = True 는 디비 안에 허용 
> 
> blank = True 는 필드가 폼 ( 입력 방식 )에 빈 채로 저장되는 것을 허용 폼에는 디비에는 '' 로 저장이 된다. // 오브젝트 생성시에 존재하지 않아도 된다.

null 이 인스턴스를 생성할 때 쓸 수 있는거구나


* DateTimeField 

> auto_now_add (True or False) 해당 레코드 생성 시 현재 시간 자동 생성 ( 객체가 처음 세이브 될 때의 시간 저장)
> auto_add (True or False) 해당 레코드 갱신 시 현재 시간 자동 저장 ( 객체의 save()가 호출 될 때 마다 저장 )

### 주요 필드 옵션
* 필드옵션 : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
* null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
* unique (DB 옵션) : 유일성 여부 (디폴트 : False)
* blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
* default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
* verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
* validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
* choices (form widget 용) : select box 소스로 사용
* help_text (form widget 용) : 필드 입력 도움말
* auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장


## 관계모델에서 제한된 관계를 만드는 방법

ForeignKey 정의에서 팀의 선수 수를 제한하는 직접적인 방법은 없습니다. 그러나이 작업은 모델 작업에 약간의 작업만으로 수행 할 수 있습니다.

한 가지 옵션은 Team에서 메소드를 만드는 것입니다.

def add_player(self, player):
    if self.player_set.count() >= 12:
         raise Exception("Too many players on this team")

    self.player_set.add(player)
그런 다음이 방법을 통해 항상 플레이어를 추가하려고합니다.


## django templates 

* 이미지 절대경로 지정 ```<img src="{{ post.image.url}}">```
 
> 해당 post 이미지의 절대 경로를 가져온다 

* html에서 파일을 전송할 때에는 반드시

><input enctype = "multipart/form-data" name = "photo"



기사 목록 꾸밀 bootstarp

```
<div class = 'container mt-2">
 {% for post in posts %}
 	<div class ="card mb-2">
 		<div class="card-body">
 			<h5 class = "card-title">{{post.title}}</h5>
 			<h6 class = "card-subtitle mb-2 text-muted">{{post.created_date }} </h6>
 			<p class = "card-text">{{post.text}}</p>
 			<p class = "text-right">Author:{{post.author}}</p>
 		</div>
	<div>
	{% endfor %}
</div>
```

## 세션과 쿠키
HTTP 프로토콜은 비 연속적이다.
>	서버에서 클라이언트에 대한 unique한 value 를 저장 -> 세션
	서버에 특정 키가 전달이 되면 유저는 클라이언트인 것으로 처리하도록 저장한다.


쿠키
>	브라우저에 저장된 값이다.
>	HTTP 요청을 보낼 때 마다 해당 값을 항상 요청에 담아서 보낸다. (도메인 기준)
>	Header 부분에 담아서 보낸다.

https://github.com/Fastcampus-WPS-9th/Instagram/blob/f714808a06a787d30a4dee4d591721ee3dbf69a3/app/templates/posts/post_list.html
강사님 깃
	
## 부트스트랩
https://getbootstrap.com/docs/4.1/getting-started/introduction/

## MVC로 패턴을 나누는 이유
모델, 뷰 , 컨트롤을 따로 짜는 이유
유지보수 관리 및 코드가 각자의 역할을 하기 위해
폼은 데이터를 검증해주는 역할이다
- 데이터를 받는 역할을 폼은 가지고 있다. 
- 요청으로 부터 특정 데이터를 받는 역할도 있다. (request)
- 받아온 데이터를 유효성 검사한다.
- 유효성 검사에 실패하였다면 그 이유를 보여준다. 
예를 들어 view에서 회원가입을 한다고 할 때
기존에 데이터베이스 안에 아이디가 있다면 중복되는 아이디라는 오류를
처리해주는 단계는 view에서도 처리 할 수 있지만, form에서 처리하는게 맞다.

## Django form view
https://docs.djangoproject.com/ko/2.2/topics/forms/

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
```

If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = NameForm(request.POST) This is called "binding data to the form" (it is now a bound form).

We call the form's is_valid() method; if it's not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

If is_valid() is True, we'll now be able to find all the validated form data in its cleaned_data attribute. We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.


### forms.form :
-required = 반드시 채워질 필요가 없다.
- validators = 특정 함수를 정의할 수 있따. ***나중에 이거 관계5명 제한할때 응용??*** [181023 18 boundForm 57:00]


### is_validation clean() method 회원가입, 로그인 에 대한 form 처리
Field 하위 클래스의 clean() 메서드는 올바른 순서로 to_python(), validate(), run_validators()를 실행하고 오류를 전파합니다. ValidationError가 발생할 때 마다 유효성 검사가 중지되고, 해당 오류가 발생합니다. 이 메서드는 cleaned_data 딕셔너리를 반환.

```python
class Form:
	field1 = forms.CharField()
	field2 = forms.IntegerField()

form = Form(reqest.POST)
form.is_valid()
이라는 간략한 과정이 있다면 form.is_valid()를 호출하는 순간
```

```
field1.clean()
	field1.to_python()
	field1.validate()
	field1.run_validators()
	return field1의 value
		-> form.cleaned_data[field1]
form.clend_field1(self):
	value = self.cleaned_data[field1]
	if User.objects.filter(value= value).exists():
		raise ValidationError('Username already exists')
	return value
field2.clean()
form.clean_field2()
필드에 대한 클린은 각각의 필드에 대한 유효성 검사를 한다.
clean_fildname은 폼 차원에서 데이터가 논리적으로 올바른 데이터를 가지고 있는지에 대한 검사.

form.clean()
이 클린은 폼에 대한 클린이다. 폼에 있는 필드들 간 데이터를 검증한다.
예를 들면 패스워드1과 패스워드2가 비밀번호가 일치하는지에 대한 검사 등을 말한다.
또는 남성인데 주민번호 뒷자리가 2로 시작하면 검증 오류를 낸다거나 이러한 것이다. 
```
```field2.clean()``` 도 위와 같이 
...
이후
```clean_<fieldname>()``` 이라는 메서드가 실행이 된다. 
```form.clean_field1()``` 과 ```form.clean_field2```가 자동으로 생성이 된다. 


```clean_<fieldname>()``` 메서드는 폼 서브 클래스에서 호출이 된다. 이 메서드는 필드의 유형과 관련이 없는 특정 속성에 특정한 모든 정리를 수행한다. 



### get_or_create

```python
obj, created = Person.objects.get_or_create(
					first_name = 'John',
					last_name = 'Lennon',
					defaults = {'birthday': date(1940, 10, 9)},
					)
first_name과 last_name에 해당하는 내용을 get 하거나
존재하지 않는다면 defaults에 포함된 내용까지 합쳐서 생성을 한다.

이 때, 두개의 값을 리턴한다 -> 튜플 (obj, created) 
get으로 가져오면 created는 False
create 로 생성하면 created 는 True

```


```
comment.tags.all()
둘은 다대다 코멘트에서 관계를 걸었음
```

```
https://whatisthenext.tistory.com/118

jyh = User.objects.get(username='jyh')
signature = SignatureTeam.objects.first()

jyh.signature.player.count()

nn = jyh.signatureteam.player

nn.all()

nn.first().name
```

### 해당하는 코멘트가 담긴 Post를 가져오는
( Post 중에서 해당 Post에 속한 Comment가 가진, HashTags들 중에서 name이 '~~~'인 Tag가 있는 Post 목록을 가져오기 )


### 내 생각에 model.py에서 is_valid와 save 메서드를 바꿔서 선수들을 추가하는 상황을 만들어야 할 듯?
1025 30 31:00

[정규표현식](https://wikidocs.net/4309)


## 쿼리 보는 방법
예제) q = Post.objects.filter(commnet__tags__name='슬기')

print(q.query)


### djagno docs Commen Web application tools에서 Customizing authenticatoin 을 하는 일반적인경우는
-> User 모델을 바꾸는 목적
기존에 서비스 중인 유저 모델에 추가로 정보를 붙여서 디비를 손봐야 하는 경우
> 프록시를 쓰거나 ( 동작 변경 )
> 
> 사용자와 관련된 정보를 더 저장해야 하는 경우 ( DB의 필드가 더 필요한 경우)에는 OtO 필드를 추가한다. 


## django docs the message framework
어떤 리퀘스트가 왔을 떄 다음번 리스펀스에 특정 내용을 담아 보내주는 역할을 한다. 

> 완료의 표시는 render를 할 때에는 그 내용을 전달 할 수 있다.-> 여러가지 데이터를 context에 담아서 보낼 수 있다. 그래서 템플릿을 통해 여러가지를 보여주는게 가능하다.
> redirect를 하면 전해줄 방법이 없다 -> 데이터를 보내서 담을 수 없기 때문이다. 브라우저에게 이동의 명령을 내리기 때문이다.

이래서 redirect의 상황에서 메세지를 보여주기 위해 message framework를 사용하게 된다. 

```
messages framework를 쓰는 경우
request
-> view( messages에 알림 데이터와 어떤 client에게 보내야 하는지를 저장한다. )
django_session 테이블에 있는 특정 session_id 값과 클라이언트(쿠키) 가 가지고 있는 session_id값을 비교해서 clien를 특정화 
-> redirect
-> view (이 client에게 message가 있다면, render 시 해당 데이터를 함께 context에 담아서 전송 )
-> render (message가 전달 한 알림 데이터를 표시)
```
## PostLike 모델 구현 이론적으로 세워보기
Like 기능
> PostList에서 작동이 가능
> 사용자의 Post의 'Like'버튼을 눌러서 좋아요 객체를 생성

Post
> 이 Post에 PostLike를 가진 User 목록
> like_users = ManyToManyField('User',
> 	# 특정 User의 기준으로 내가 like_users인 Post목록
> 	# 내가 Like를 한 Post의 목록
> 	related_name = 'like_posts'
>	related_query_name = 'like_post')

User

PostLike 객체
	user
	post
	created_at
	
## 소셜 로그인 
상세 - 가입
```
웹 사이트 A에 사용자가 접속
페이스북으로 로그인 버튼을 클릭
Django가 사용자를 페이스북에 넘겨준다. 
	우리가 너의 정보를 쓸 것인데 페이스북에서 허용을 눌러줘
	facebook.com/<로그인 관련>/<특정 APP ID>/
사용자가 페이스북에서 해당 내용에 대해 허용을 하면
페이스북이 Django에게 특정 '토큰'을 넘겨준다.
'토큰'은 특정 페이스북 사용자의 '특정권한'에 접근을 할 수 있는 '키'이다.
Django는 '토큰'을 사용하여 '특정 페이스북 사용자'의 정보를 가져와서 자신의 서비스에 DjangoUser를 생성하는데 사용한다. 
인증에 사용하는 값은 '페이스북 유저의 특정 값' <- '토큰'을 사용하여 알아낼 수 있다.	
```

상세 - 로그인 
```
웹 사이트 A에 로그인
페이스북으로 로그인 버튼 클릭
Django가 사용자를 페이스북에 넘겨준다. 
	우리가 너의 정보를 쓸 것인데 페이스북에서 허용을 눌러줘 -> 이미 눌려있으니 다음단계
'토큰'을 받아온 뒤 '토큰'을 사용하여 '특정 페이스북 사용자'의 정보를 가져와서 이미 우리가 가지고 있는 DjangoUser의 '특정 페이스북 값'과 비교 존재한다면 Django 로그인처리
```


## 구글 로그인 
### pip 초기 기본 세팅
```pip install django-allauth```

### settings.py에 입력을 할 부분
INSTALLED_APPS의 부분에 **django.contrib.sites,	allauth,	 allauth.account, 	allauth.socialaccount**를 추가하여준다. 
그리고 provider라는 것을 추가 해 줄 것인데 이것은 소셜로그인 기능을 제공해주는 서비스 업체를 프로바이더라 칭한다. 장고에서 사용할 수 있는 프로바이더는 찾아보면 정말 많이 있다. 그래서 provider.[원하는 social-soccial-service]를 추가하면 다른 소셜로그인 기능이 추가되는 개념이라 생각하면 될 것 같다.   **'allauth.socialaccount.provider.google'** 도 추가해준다.

- django.contrib.sites는 사이트 정보를 설정하기 위해서
- allauth.account 는 가입한 계정 관리를 위해서
- allauth.socialaccount는 소셜 계정으로 가입한 계정 관리
- allauth.socialaccount.providers.<서비스사이트>는 어떤 소셜서비스를 사용할지에 따라서

```python
# AUTHENTICATION_BACKENDS는 어떤 형식의 로그인을 사용할 지 정한다. allauth는 이메일을 사용하는 방식이라 한다

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
]
# 이건 전역으로 설정
SITE_ID = 1
LOGIN_REDIRECT_URL='/'
```

-------

### urls.py
django-allauth를 다운 받게 되면서 생기는 url의 패턴을 추가한다
```path('accounts/', include('allauth.urls')),```
이미 존재하는 url 이므로 이 안에서 소셜로그인을 통한 처리는 일어난다. 

-------
settings.py 와 urls.py의 내용을 추가하였다면 

1. ```./manage.py migrate 실행```하고 

2. runserver , local/admin에 들어가서 마이그레이션이 잘 되었나 확인을 해보자 site, social accoutn, authentication and authorization 등이 추가 되었을 것이다

### admin 설정 - 구글
- sites에 들어가서 example에 있는 주소를 로컬기준 127.0.0.1:8000으로 도메인 명과 표시 명을 바꾸어 준다. 

- 홈>소셜 계정 >소셜 어플리케이션 > 소셜 어플리케이션 추가 
- 의 페이지로 들어가서 제공자(provider)에 해당 사이트 ( setting.py에서 추가한 사이트가 뜰 것임 )
- 이름은 원하는대로
- 클라이언트와 비밀키는 해당 사이트에서 발급받아야 함
- ```console.developers.google.com``` 에 들어가서 소셜로그인을 위한 승인과정을 거친다.              

- 앱을 만들고
- 사용자 인증정보에서 OAuth 클릭
- 그런 다음 동의화면구성을 누르고
- 동의화면에서 애플리케이션 이름을 정한다
- 그 다음 사용자 인증정보에서 다시 OAuth클릭
- 애플리케이션 유형은 웹을 누르고 제한사항에서 자바스크립트 원본과 리디렉션은 로컬기준으로 http://localhost:8000



- 그리고 저장을 누르면 클라이언트 ID와 키가 발급된다.**클라이언트 아이디와 키를 끄지 말고 이 상태에서 django-admin으로 돌아와서 키를 넣어야 한다.**
- 다시 admin의 홈>소셜 계정 >소셜 어플리케이션 > 소셜 어플리케이션 추가 의 페이지로 돌아와서 클라이언트 ID와 비밀키를 기입한다.
- 여기서 기존에 이미 만들었다면 ```console.developers.google.com``` 페이지에서 해당 ID에 들어가 클라이언트 아이디와 시크릿 패스워드를 알아낸다
- 그리고 이용 가능한 사이트에 있는 목록에서 선택된 사이트로 더블클릭 또는 화살표 ui를 통해서 이동시킨다.
- 그리고 저장을 누른 뒤 html을 작성하자.
#### login-page for html

```python
{% load socialaccount %} 이걸 로그인하는 html의 맨 위에 둔다
{% extends 'base.html'%} 이 존재한다면 그 아래에 둔다
socialaccount 기능을 쓰기 위한 코드


# 로그인 버튼 자리 안에 넣어준다.
<a href="{% provider_login_url 'google' %}">구글 로그인</a>
이 a태그를 추가하면 구글 로그인을 수행하여 준다.

# <a href="/accounts/signup">구글 회원가입</a><br> 이건 allauth에서 지원해주는 회원가입 기능으로 보내주는 태그l
```

오류 발생시 
callback에러
>```console.developers.google.com```에서 OAuth        클라이언트ID 만들기 과정 속에 있던 승인된 리디렉션 URI에
>http://localhost:8000/accounts/google/login/callback/
>를 추가하여준다.


### 설정 - 네이버
#### settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
]


## RDS 설정 
Django 와 연관성이 좋은 postgre-sql 
postgreSQL은 기본적으로 5432 포트를 쓰게 되어있다.

설정 사항들 

- 템플릿 - 프리티어
- 디비 인스턴스 크기 	버스터블 	t클래스 t2.micro
- 스토리지 할당 20 , 자동 조정 비활성화 
- 다중 AZ 배포 비활성화 
- VPC는 ECS를 위해 따로 만들었던 로드벨런서 
- 퍼블릭 엑세스는 yes
- EC2 보안그룹은 새로 생성하고 이름은 :```RDS Security Group```

```python
# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '<RDS에 생성 된 엔드포인트>', 
        'NAME': '<RDS 설정 시 데이터베이스 이름>',
        'USER': '<RDS 설정 시 master username>',
        'PASSWORD': '<RDS 설정 시 암호>',
        'PORT': 5432,
    }
}
# postgresql은 기본적으로 포트 5432를 쓰게 되어있다.
# 네임은 RDS 설정 시 데이터베이스 이름
# 유저는 RDS 설정 시 master username
```

## 에러 상황
- export config/settings/dev 에서 ./manage.py 상황 시, psycopg2에 대한 모듈 에러가 발생한다면 이것은 Django에서 postgresql을 사용할 수 있도록 도와주는 라이브러리이다. 
```pip install psycopg2-binary``` 를 쉘에서 실행하면 된다. 

- ```could not connect to server timed out```은 EC2 보안그룹에서 아까 생성 하였던, RDS Security Group을 클릭 한 뒤 인바운드 편집에서 ```편집 ->``` 유형은 postgre 포트 5432 소스는 원하는 상황으로 한 뒤 다시 app에서 ./maange.py migrate하면 된다. 

## settings 변경
> .secrets에 DATABAES에 대한 정보를 저장 한 뒤, settings에서 불러오는 것을 추천한다. 

```python
# ex )proj/app/config/settings/dev.py
dev_secrets = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

DATABASES = dev_secrets['DATABASES']


# proj/.secrets/dev.json
{
	"DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      	 "HOST": "<RDS에 생성 된 엔드포인트>", 
        "NAME": "<RDS 설정 시 초기 데이터베이스 이름>",
        "USER": "<RDS 설정 시 master username>",
        "PASSWORD": "<RDS 설정 시 암호>",
      "PORT": 5432
    }
  }
}
```

- 개발용 디비와 서비스용 디비는 가르는 것이 좋다. 
- 데이터베이스 서버와 서버 안에 데이터베이스들이 여러개가 있는 것은 다른것임을 우리는 안다. 

## DB 접속하기 - psql

1. 쉘 ```mac 기준 brew install postgresql```
2. 쉘 ```psql --user=<RDS user> --host=<엔드포인트> postgres```
3.  비밀번호 입력 후 접속
4.  디비를 나누기 원한다면 CREATE DATABASE <DB명> OWNER <user>;
5. \l을 누르면 목록이 나온다
6. 생성한 디비에 접속하고 싶다면 생성한 디비명을 아까 2번의 명령어 뒤의 postgresql을 지우고, 생성한 디비명을 입력한다. 
7. 분리를 하였다면, .secrets에 있는 dev나 production의 DATABASES NAME을 생성한 디비명으로 바꾸어준다.


만약 접속이 안될시 장소를 바꾼 것이라면 EC2의 보안그룹에서 RDS Security Group의 인바운드를 추가해준다. 


## SocialApp matching query does not exist. 에러 발생
SocialApp matching query does not exist.

![ERD](/assets/SocialApp/SocialApp.png)
이 발생한다면 디비를 엎은 후, admin에 설정이 없기 때문 다시 가서 클라이언트 아이디와 패스워드를 받아온다. 


## search 기능 구현
```python
def tag_post_list(request, tag_name):
    # Post중, 자신에게 속한 Comment가 가진 HashTag 목록 중 tag_name 이 name인 HashTag가 포함 된
    # Post 목록을 posts 변수에 할당
    # context 에 담아서 리턴 render
    # HTML: /posts/tag_post_list.html

    posts = Post.objects.filter(comments__tags__name=tag_name).distinct() | \
            Post.objects.filter(postTags__name=tag_name).distinct()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/tag_post_list.html', context)

```
> post 페이지에서 검색한 값이 해시태그로 작성된 댓글이면 검색이 가능하도록 해주는 것이 기존의 서비스였다.
> 
> 댓글의 해시태그 뿐 아닌, 게시글에 존재하는 태그도 검색이 가능하도록 하는것을 원하였다. 
> 
> **Post.objects.filter(comments__tags__name=tag_name or postTags__name=tag_name).distinct()**
> 
> 이 가능할 것 이라고 생각하였지만 **or**은 문법상의 오류로 인식, 기능 구현이 되지 않았다 **|** or 의 표현식을 통해 가능하였다. 


## nginx 504 Gateway Time-out 에러 발생 시 대처 방법

>DB를 sqlite를 사용하는 상황에서 배포와 로컬에서 작동은 이상이 없었지만, docker run의 상황속에서 504 에러가 발생하였다.
>
>구글링을 통해 해결한 방법은 [해당링크](https://jootc.com/p/201806101238)를 통해 해결 하였다.



 ```python
location / {
    proxy_connect_timeout 300;
    proxy_send_timeout 300;
    proxy_read_timeout 300;
    send_timeout 300;
}```

