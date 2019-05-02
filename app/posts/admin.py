from django.contrib import admin

# Register your models here.
from posts.models import *


class SignatureTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', ]

    ordering = ['pk']

    def add_player(self,request):
        if self.player.count() > 5:
            raise Exception("Too many players on this User")
        self.Player.add(request.player)


admin.site.register(SignatureTeam, SignatureTeamAdmin)


admin.site.register(Post)
admin.site.register(Postlike)
admin.site.register(Comment)
admin.site.register(HashTags)