from django.contrib import admin

# Register your models here.
from posts.models import *

admin.site.register(Post)
admin.site.register(Postlike)
admin.site.register(Comment)
admin.site.register(HashTags)
