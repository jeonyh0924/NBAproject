from django.contrib import admin

# Register your models here.
from challengepost.models import *

admin.site.register(challengePost)
admin.site.register(challengeComment)
admin.site.register(challengePostLike)