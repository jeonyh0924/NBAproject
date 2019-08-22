import requests
from .base import *

production_secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

DEBUG = True

# 아마존에서 제공해주는 URL에 접속을 허용하는 코드
ALLOWED_HOSTS = production_secrets['ALLOWED_HOSTS']

# postgreSQL - RDS
# DATABASES = production_secrets['DATABASES']

# SQlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# s3 버전 및 지역 설정
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'

# s3
AWS_STORAGE_BUCKET_NAME = production_secrets['AWS_STORAGE_BUCKET_NAME']

# .static 을 Storage 공간으로 사용하려면 아래 설정을 주석 처리 해야한다.
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
AWS_ACCESS_KEY_ID = production_secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = production_secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = production_secrets['AWS_STORAGE_BUCKET_NAME']
# Health Check 도메인을 허용하는 코드
try:
    EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass

WSGI_APPLICATION = 'config.wsgi.production.application'
