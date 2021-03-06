from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models

# Create your models here.

from members.models import Player


class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to='author',
        blank=True
    )
    introduce = models.TextField(max_length=300, blank=True, null=True)

    like_player = models.ManyToManyField(
        Player,
        through='Challenge',
        related_name='like_users',
        related_query_name='like_user',
    )

    def __str__(self):
        return self.username

    @property
    def img_profile_url(self):
        if self.img_profile:
            return self.img_profile.url
        return static('images/user.png')

    def like_post_toggle(self, post):
        # 자신에게 연결된 PostLike 중 , post 값이 매개변수의 post인 PostLike가 있다면 가져오고 없으면 생성
        postlike, postlike_created = self.postlike_set.get_or_create(post=post)
        if not postlike_created:
            postlike.delete()


class Challenge(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=10, blank=True, null=True)
