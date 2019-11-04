"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')
# .secrets/base.json에 있는 데이터를 파싱하여 파이썬 dict가져옴
secrets = json.load(open(os.path.join(SECRET_DIR, 'base.json')))
# Django secret key
SECRET_KEY = secrets['SECRET_KEY']

FACEBOOK_APP_ID = secrets['FACEBOOK_APP_ID']
FACEBOOK_APP_SECRET = secrets['FACEBOOK_APP_SECRET']

STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, '.static/admin'),
    os.path.join(ROOT_DIR, '.static/bootstrap'),
    os.path.join(ROOT_DIR, '.static/images'),
    # os.path.join(ROOT_DIR, 'app/static/images'),
    # 이전에 했던게 이거
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

# login_reuquired 데코레이터에 의해 로그인 페이지로 이동해야 할 때, 그 이동 할 URL의 URL pattern name
LOGIN_URL = 'users:login'

# social_login_google - allauth
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# authenticate() 함수를 호출 시 사용할 백엔드 목록
AUTHENTICATION_BACKENDS = [
    # 리스트말고 튜플이라는데 좀 이따가 안되면 수정해보
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.FacebookBackEnd',
    # allauth
    'allauth.account.auth_backends.AuthenticationBackend',
]

CRONJOBS = [
    ('*/26 * * * *', 'BASE_DIR.cron.my_cron_job')
]

# Auth
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django_celery_beat',
    'django_celery_results',
    'django_crontab',

    'shop',
    'cart',
    'challengepost.apps.ChallengepostConfig',
    'users.apps.UsersConfig',
    'posts.apps.PostsConfig',
    'members.apps.MembersConfig',
    'news',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    # allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True
# USE_TZ 값이 True이면 DB에 저장할 하거나 화면에 출력할 때 +/-9시간을 계산합니다.
USE_TZ = True

CART_ID = 'cart_in_session'
