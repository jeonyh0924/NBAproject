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
}

```

#### 6월 중순에 학기가 끝나고 readme에 정리한 내용들을 깃 블로그에 정리해서 올릴 것 입니다. 

## settings.py
STATICFILES_DIRS = [
    STATIC_DIR,
]
1. 개발 모드에서 settings.STATIC_URL 에 해당하는 request는
2. settings.STATICFILES_DIRS 리스트 내의 경로목록 각각의 하위 위치에서 해당 파일을 검색하며 존재한다면 그 파일을 리턴해준다. 

### 크롤링 사이트 참고 - 파일 경로 설정
https://thispointer.com/how-to-create-a-directory-in-python/
### 셀리니움 
https://selenium-python.readthedocs.io/locating-elements.html


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
https://www.slideshare.net/bbayoung7849/djangoadminsitecustomexample  박영우 님의 파이콘 한국 2017 발표자료

https://teamlab.github.io/jekyllDecent/blog/tutorials/Django-Admin-%EC%BB%A4%EC%8A%A4%ED%84%B0%EB%A7%88%EC%9D%B4%EC%A7%95
장고 어드민 스타일링

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

