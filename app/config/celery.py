import os

from celery import Celery
from celery.schedules import crontab

# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery(
    'config',
    broker='redis://localhost:6379/0',
)

# 문자열로 등록한 이유는 Celery Worker가 자식 프로세스에
# configuration object를 직렬화하지 않아도 된다는 것 때문
# namespace = 'CELERY'는 모든 celery 관련한 configuration key가
# 'CELERY_' 로 시작해야함을 의미함
app.config_from_object('django.conf:settings', namespace='CELERY')

# task 모듈을 모든 등록된 Django App config에 load함
app.autodiscover_tasks()

app.conf.update(
    BROKER_URL='redis://localhost:6379',
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Asia/Seoul',
    CELERY_ENABLE_UTC=False,
    CELERYBEAT_SCHEDULE={
        'add-first-of-every-month': {
            'task': 'news.tasks.headlines_crawling',
            # 10분 간격 실행
            'schedule': crontab(minute='*/10'),
            # 매일 자정 실행
            # 'schedule': crontab(minute=0, hour=0),
            'args': (),
        },
    }
)


# bing=True 옵션을 주게 되면
# 아래 함수의 인자에 self가 추가됨 ==> 'self'는 관용적으로 쓰임
# 이 앱의 실행시켰을때에 대한 정보가 담겨져옴

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
