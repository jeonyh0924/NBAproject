from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.production.application'

DATABASES = secrets['DATABASES']

# .static 을 Storage 공간으로 사용하려면 아래 설정을 주석 처리 해야한다.
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# s3 버전 및 지역 설정
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
