from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    ordering = ['pk']

    def __unicode__(self):
        return self.name


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'back_number', 'position', 'team']
    list_per_page = 10
    list_filter = ['team', 'id']
    ordering = ['pk', ]
    search_fields = ['team__name', 'back_number', ]

    fieldsets = (
        ('소속 팀', {
            'fields': ('team',)
        }),
        ('선수 스탯', {
            'fields': (
                'playin_time', 'FGP', 'T3PP', 'FTP', 'PPG', 'RPG', 'APG', 'BPG',
            )
        }),
        ('선수 프로필', {
            'fields': (
                'name', 'back_number', 'position', 'first_name', 'last_name', 'height', 'weight',
                'born', 'hometown', 'nba_debut', 'image',
            )
        })
    )

    def __unicode__(self):
        return self.name

    # def player_crawling(mo):
    #     crawling = Player.crawler()

    # player_crawling().short_description = "선수 오브젝트 생성"