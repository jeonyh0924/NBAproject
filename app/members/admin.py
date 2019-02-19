from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    ordering = ['pk']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'back_number', 'position', 'team']
    list_per_page = 40
    list_filter = ['team', 'id']
    ordering = ['pk']
