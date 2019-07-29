from .models import newsHeadlines
from config import celery_app


@celery_app.task
def headlines_crawling():
    newsHeadlines.crawler()
    print('종료')
