from django.urls import path
from . import views

app_name = 'challengepost'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('detail/(?P<post_pk>[0-9]+)/', views.post_detail, name='detail'),
    path('<int:post_pk>/comments/create/', views.comment_create, name='comment-create'),
    path('create/', views.post_create, name='create'),
    path('<int:post_pk>/like-toggle/', views.post_like_toggle, name='post-like-toggle'),
]
