from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


def team_image_path(instance, filename):
    directory = instance.title
    return f'{directory}/{filename}'


class Team:

    def SetData(self, name, img):
        self.name = name
        self.img = img

    def __init__(self, name, img):
        self.SetData(name,img)
        print('Team이 생성되었습니다.')
    name = models.CharField(max_length=20,verbose_name='팀 이름')
    img = models.ImageField(upload_to=team_image_path, blank=True, null=True, verbose_name='메인 포스터')

