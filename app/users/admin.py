from django.contrib import admin

# Register your models here.
from .models import *


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


admin.site.register(User, UserAdmin)
