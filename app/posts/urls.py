from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:post_pk>/', views.post_detail, name='post-detail'),
    path('create/', views.post_create, name='post-create'),
    path('<int:post_pk>/comments/create/', views.comment_create, name='comment-create'),
    path('explore/tags/<str:tag_name>/', views.tag_post_list, name='tag-post-list'),
    path('tag-search/', views.tag_search, name='tag-search'),
    path('<int:post_pk>/like-toggle/', views.post_like_toggle, name='post-like-toggle'),
]
