from django.contrib import admin

from posts.models import SignatureTeam
from .models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    ordering = ['pk']

    def __unicode__(self):
        return self.name

    def make_team_objects(Teammodel, request, query):
        Team.crawler()

    actions = [make_team_objects]

    make_team_objects.short_description = "팀 크롤링 실행"


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    def __unicode__(self):
        return self.name

    def make_objects(ModelAdmin, request, queryset):
        Player.crawler()

    make_objects.short_description = "선수 크롤러 실행"

    list_display = ['id', 'first_name', 'last_name', 'back_number', 'position', 'team']
    list_per_page = 15
    list_filter = ['team', 'position']
    ordering = ['pk', ]
    actions = [make_objects]
    search_fields = ['team__name', 'back_number', 'name']

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

