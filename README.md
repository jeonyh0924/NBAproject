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

## django modeling 정리
* Foreignkey (on_delete = model.CASECADE)
>모델 A와 모델 B가 M:1 관계일 때, 모델 A에 on_delete = model.CASECADE가 설정되어 있으면, 모델 B의 어떤 레코드가 삭제되면 삭제될 모델 B의 레코드와 관련된 모델 A의 레코드도 삭제된다. 

>즉 지워질 때, 같이 지워지게 종속관계를 설정하는 것, 
>선수 모델이 팀 모델에 외래키를 걸고 CASECADE 설정을 하게 되면
>선수 모델이 제거될 때 팀 모델 또한 삭제된다. 

* Null 과 blank 차이 

> 필드를 비워둘 것인지 허용하는 방법
> Null = True 필드의 값이 Null ( 정보 없음 ) 으로 저장되는 것을 허용한다. null = True 는 디비 안에 허용 
> 
> blank = True 는 필드가 폼 ( 입력 방식 )에 빈 채로 저장되는 것을 허용 폼에는 디비에는 '' 로 저장이 된다. 

null 이 인스턴스를 생성할 때 쓸 수 있는거구나
