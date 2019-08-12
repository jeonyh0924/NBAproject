from django.contrib import admin

# Register your models here.
from .models import newsHeadlines, Person, Group, Membership

admin.site.register(newsHeadlines)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)