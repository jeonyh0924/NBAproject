import re

from django.contrib.auth.models import AbstractUser
from django.db import models

from members.models import post_path
from users.models import *


class Post(models.Model):
    TAG_PATTERN = p = re.compile(r'#(?P<tag>\w+)')
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    title = models.TextField(verbose_name='제목', max_length=40)
    content = models.TextField(verbose_name='작성 글', max_length=500)
    tag = models.TextField(verbose_name='태그', max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성 날짜', auto_now_add=True, )
    # auto now add 는 객체가 save 될 때 마다 호
    updated_at = models.DateTimeField(verbose_name='수정 날짜', auto_now=True, null=True, blank=True)
    image = models.ImageField(upload_to='post', verbose_name='업로드 이미지', blank=True, null=True, default=True)
    postTags = models.ManyToManyField('HashTags', blank=True, )
    _html = models.TextField('태그가 html화 된 댓글 내용', blank=True)

    like_users = models.ManyToManyField(
        User,
        through='Postlike',
        related_name='like_posts',
        related_query_name='like_post',
    )

    # 업로드 투 post_path 이거에서 바꿔봄

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'
        ordering = ['-pk']
        # 생성의 역순 desc

    def save(self, *args, **kwargs):
        def save_html():
            # 저장하기 전에 _html 필드를 채워주어야 한다. ( content 값을 사용해서 )
            self._html = re.sub(self.TAG_PATTERN, r'<a href="/posts/explore/tags/\g<tag>/">#\g<tag></a>', self.tag, )

        def save_tags():
            # DB에 Comment
            # 자신의 'tag' 값에서 해시태그 목록을 가져와서
            # 자신의 'postTags'속성 (MTM 필드)에 해당
            tags = [HashTags.objects.get_or_create(name=name)[0] for name in re.findall(self.TAG_PATTERN, self.tag)]
            self.postTags.set(tags)

        save_html()
        super().save(*args, **kwargs)
        save_tags()

    @property
    def html(self):
        # 자신의 tag 값에서
        # "#태그명"에 해당하는 문자열을
        # 아래와 같이 변
        # 문자열 -> <a href="/explore/tags/{태그명}/"> #{태그명}</a>
        # re.sub를 사용

        # 템플릿에서는 post.html 출력
        # 숙제
        #  /explore/tags/{태그명}/ URL에서
        #  해당 태그를 가진 Post목록을 보여주는 view, url, template구현
        #  URL name: tag-post-list
        #  view:
        #       tag_post_list(request, tag_name)
        #  template:
        #       /posts/tag_post_list.html

        # base.html에 있는 검색창에 값을 입력하고 Enter시 (Submit)
        #  해당 값을 사용해 위에서 만든 view로 이동
        return self._html

    def like_toggle(self, user):
        postlike, postlike_created = self.postlike_set.get_or_create(user=user)
        if not postlike_created:
            postlike.delete()


class Comment(models.Model):
    TAG_PATTERN = p = re.compile(r'#(?P<tag>\w+)')

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트',
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    content = models.TextField(verbose_name='댓글 내용', max_length=500)
    tags = models.ManyToManyField(
        'HashTags',
        blank=True,
    )
    # 글쓴이
    created_at = models.DateTimeField(verbose_name='작성 날', auto_now_add=True, )
    updated_at = models.DateTimeField(verbose_name='수정 날짜', auto_now=True, )

    # save 가 호출될 시 content의 값을 사용해서 이 필드를 자동으로 채운 후 저장한다.
    _html = models.TextField('태그가 html화 된 댓글 내용', blank=True)

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'

    def save(self, *args, **kwargs):
        def save_html():
            self._html = re.sub(self.TAG_PATTERN, r'<a href="/posts/explore/tags/\g<tag>/">#\g<tag></a>',
                                self.content, )

        def save_tags():
            tags = [HashTags.objects.get_or_create(name=name)[0] for name in re.findall(self.TAG_PATTERN, self.content)]
            self.tags.set(tags)

        save_html()
        super().save(*args, **kwargs)
        save_tags()

    @property
    def html(self):
        # 자신의 tag 값에서
        # "#태그명"에 해당하는 문자열을
        # 아래와 같이 변
        # 문자열 -> <a href="/explore/tags/{태그명}/"> #{태그명}</a>
        # re.sub를 사용

        # 템플릿에서는 post.html 출력
        # 숙제
        #  /explore/tags/{태그명}/ URL에서
        #  해당 태그를 가진 Post목록을 보여주는 view, url, template구현
        #  URL name: tag-post-list
        #  view:
        #       tag_post_list(request, tag_name)
        #  template:
        #       /posts/tag_post_list.html

        # base.html에 있는 검색창에 값을 입력하고 Enter시 (Submit)
        #  해당 값을 사용해 위에서 만든 view로 이동
        return self._html


class HashTags(models.Model):
    name = models.CharField('태그명', max_length=100, unique=True, )

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

    def __str__(self):
        return 'Post[{post_pk}] Like (User: {username})'.format(
            post_pk=self.post.pk,
            username=self.user.username,
        )

    class Meta:
        verbose_name = '게시글 좋아요'
        verbose_name_plural = f'{verbose_name} 목록'
        # 특정 유저가 특정 포스트 좋아요를 누른 정보는 유니크 해야 함.
        unique_together = (
            ('post', 'user'),
        )
