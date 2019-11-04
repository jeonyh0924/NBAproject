from django.db import models

# Create your models here.

from config.settings.base import AUTH_USER_MODEL
from users.models import User


class challengePost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField(null=True, blank=True)
    # auto_now_add: 객체가 처음 생성될때의 시간 저장
    # auto_now: 객체의 save()가 호출될 때 마다 시간 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        AUTH_USER_MODEL,
        through='challengePostLike',
        related_name='challengelike_posts',
        related_query_name='challengelike_post',
    )

    class Meta:
        verbose_name = '선수단 포스트'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    def like_toggle(self, user):
        postlike, postlike_created = self.challengepostlike_set.get_or_create(user=user)
        if not postlike_created:
            postlike.delete()


class challengeComment(models.Model):
    post = models.ForeignKey(
        challengePost,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class challengePostLike(models.Model):
    post = models.ForeignKey(
        challengePost,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post[{post_pk}] Like (User: {username})'.format(
            post_pk=self.post.pk,
            username=self.user.username,
        )

    class Meta:
        # 특정 User가 특정 Post를 좋아요 누른 정보는 unique해야함
        unique_together = (
            ('post', 'user'),
        )
