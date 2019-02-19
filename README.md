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
