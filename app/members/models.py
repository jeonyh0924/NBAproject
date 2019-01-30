from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


def team_image_path(instance, filename):
    directory = instance.title
    return f'{directory}/{filename}'


class TeamManager(models.Manager):

    def create_Team(self,name):
        team = self.create(name=name)
        return team


class Team(models.Model):
    name = models.CharField(max_length=30)
    objects = TeamManager()
