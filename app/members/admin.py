from django.contrib import admin
from .models import *


#
# @admin.register(PlayerRoster)
# class PlayerRosterAdmin(admin.ModelAdmin):
#     list_display = ['player', 'roster', 'create_date', 'update_date',
#                     ]
#     fieldsets = (
#         ('PlayerRoster', {
#             'fields': (
#                 'player', 'roster',
#             )
#         }),
#     )


@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ['name']

    fieldsets = (
        ('선수', {
            'fields': (
                'name',
            )
        }),
    )


@admin.register(PlayerOption)
class PlayerOptionAdmin(admin.ModelAdmin):
    list_display = ['value', 'type']

    def make_option(self, request, query):
        PlayerOption.make_dollars()

    actions = [make_option]

    make_option.short_description = "달러 생성"

    fieldsets = (
        ('values', {
            'fields': (
                'value', 'type',
            )
        }),
    )


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

    list_display = ['id', 'first_name', 'last_name', 'back_number', 'position', 'team', ]
    list_per_page = 15
    list_filter = ['team', 'position']
    ordering = ['pk', ]
    actions = [make_objects]
    search_fields = ['team__name', 'back_number', 'name']

    fieldsets = (
        ('챌린지', {
            'fields': ('playeroption',)
        }),
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
