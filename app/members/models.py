from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass




class Team(models.Model):
    name = models.CharField(verbose_name='팀 이름', max_length=100)
    team_image = models.ImageField(verbose_name='팀 사진', blank=True, null=True, default=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    # 선수 스탯
    playin_time = models.CharField(verbose_name='출장 시간', max_length=100)
    FGP = models.FloatField(verbose_name='야투 성공률', default=0)
    T3PP = models.FloatField(verbose_name='3점 야투 성공률', default=0)
    FTP = models.FloatField(verbose_name='자유투 성공률', default=0)
    PPG = models.FloatField(verbose_name='게임 평균 득점', default=0)
    RPG = models.FloatField(verbose_name='게임 평균 리바운드', default=0)
    APG = models.FloatField(verbose_name='게임 평균 어시스트', default=0)
    BPG = models.FloatField(verbose_name='게임 평균 블락', default=0)

    # 선수 프로필
    player_back_number = models.CharField(verbose_name='선수 등 번호', max_length=100)
    player_position = models.CharField(verbose_name='선수 포지션', max_length=5)
    player_first_name = models.CharField(verbose_name='선수 이름', max_length=50)
    player_last_name = models.CharField(verbose_name='선수 성씨', max_length=50)
    player_height = models.CharField(verbose_name='선수 키', max_length=100)
    player_weight = models.CharField(verbose_name='선수 무게', max_length=100)
    player_born = models.CharField(verbose_name='선수 생년월일', max_length=50)
    player_hometown = models.CharField(verbose_name='선수 고향', max_length=50)
    player_nba_debut = models.CharField(verbose_name='데뷔 년도', max_length=50)
    player_image = models.ImageField(verbose_name='선수 사진', blank=True, null=True, default=True)

    def __str__(self):
        return self.name

