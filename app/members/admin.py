from django.contrib import admin

from .models import *

admin.site.register(User)


# admin.site.register(Signature_team)


class UserAdmin(admin.ModelAdmin):
    def make_default_user(modeladmin, request, query):
        for i in range(1, 51):
            User.objects.create(
                username=f"test{i}",
                password=1111,
                first_name=f"{i}",
                last_name=f"tester",
                email=f"tester{i}@test.com",

            )

    make_default_user.short_description = "기본 테스트 유저 생성"
    model = User
    ordering = ['pk', ]
    actions = [make_default_user]
    list_display = (
        'username',
        'get_name',
    )

    def get_name(self, obj):
        return obj.last_name + obj.first_name


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


@admin.register(Signature_team)
class Signature_team(admin.ModelAdmin):
    list_display = ['id', 'user', ]

    ordering = ['pk']


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
