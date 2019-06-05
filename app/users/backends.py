import imghdr

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class FacebookBackEnd:
    def authenticate(self, request, facebook_request_token):
        # URL: /users/facebook-login/
        # URL name: 'users:facebook-login'
        # request.GET에 전달 된 'code'값을 그대로 HttpResponse 로 출력
        # 페이스북 로그인 버튼의 href 안에 있는 'redirect_uri' 값을 이 view 로 오도록 출력
        api_base = 'https://graph.facebook.com/v3.3'
        api_get_access_token = f'{api_base}/oauth/access_token'
        api_me = f'{api_base}/me'
        # 페이스북 request token

        # code = request.GET.get('code')
        code = facebook_request_token
        # request token

        # request token을 access 토큰으로 교환
        params = {
            'client_id': settings.FACEBOOK_APP_ID,
            'redirect_uri': 'http://localhost:8000/users/facebook-login/',
            'client_secret': settings.FACEBOOK_APP_SECRET,
            'code': code,
        }
        response = requests.get(api_get_access_token, params)
        # 인수로 전달한 문자열이 'JSON' 형식일 것 이라고 생각
        # json.loads 전달할 문자열 JSON 형식일 경우, 해당 문자열을 parsing 하여 파이선 objects를 리턴한다.
        # response_objects = json.loads(response.text)
        data = response.json()
        access_token = data['access_token']

        # access_token을 사용하여 사용자의 정보 가져옴
        params = {
            'access_token': access_token,
            'fields': ','.join([
                'id', 'first_name', 'last_name', 'picture.type(large)',
            ])
        }
        response = requests.get(api_me, params)
        data = response.json()
        facebook_id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        url_img_profile = data['picture']['data']['url']
        # HTTP GET 요청의 응답을 받아와서 binary data 를 img_data 변수에 할
        img_response = requests.get(url_img_profile)
        img_data = img_response.content

        # imghdr 모듈을 사용하여 Image binary data 의 확장자를 알아
        ext = imghdr.what('', h=img_data)

        # Form 에서 업로드 한 것과 같은 형태의 file-like object 생성
        # 첫 번째 인수로 반드시 파일명이 필요, <facebook_id>.<확장자> 형태의 파일명을 지
        f = SimpleUploadedFile(f'{facebook_id}.{ext}', img_response.content)

        try:
            user = User.objects.get(username=facebook_id)
            user.last_name = last_name
            user.first_name = first_name
            # user.img_profile = f
            user.save()
        except User.DoesNotExist:
            User.objects.create_user(
                username=facebook_id,
                first_name=first_name,
                last_name=last_name,
                img_profile=f,
            )
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
