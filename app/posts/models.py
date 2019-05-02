from django.contrib.auth.models import AbstractUser
from django.db import models

from members.models import post_path
from users.models import *


class Post(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    content = models.TextField(verbose_name='작성 글', max_length=500)
    created_at = models.DateTimeField(verbose_name='생성 날짜', auto_now_add=True, )
    # auto now add 는 객체가 save 될 때 마다 호
    updated_at = models.DateTimeField(verbose_name='수정 날짜', auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='post', verbose_name='게시글 이미지', blank=True, null=True, default=True)
    # 업로드 투 post_path 이거에서 바꿔봄

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'
        ordering =['-pk']
        # 생성의 역순 desc


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        'HashTags',
        blank=True,
    )
    # 글쓴이
    content = models.TextField(verbose_name='작성 글', max_length=500)
    created_at = models.DateTimeField(verbose_name='작성 날', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='수정 날짜', auto_now=True, )

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'


class HashTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '해시태그'
        verbose_name_plural = f'{verbose_name} 목록'


class SignatureTeam(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    player = models.ManyToManyField(Player, blank=True, null=True)

    def add_player(self, player):
        if self.player.count() >= 6:
            raise Exception("Too many players on this User")
        self.player.add(player)

    class Meta:
        verbose_name = '유저 지정 팀'
        verbose_name_plural = f'{verbose_name} 목록'


class Postlike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = '게시글 좋아요'
        verbose_name_plural = f'{verbose_name} 목록'
        # 특정 유저가 특정 포스트 좋아요를 누른 정보는 유니크 해야 함.
        unique_together = (
            ('post', 'user'),
        )
