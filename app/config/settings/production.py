from .base import *

secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}