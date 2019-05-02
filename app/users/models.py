from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from members.models import Player


class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to='author',
        blank=True
    )
    introduce = models.TextField(max_length=300, blank=True, null=True)
    player = models.ManyToManyField(Player, blank=True, null=True)

    def __str__(self):
        return self.username