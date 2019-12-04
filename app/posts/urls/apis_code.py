from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import apis_code as views

# app_name = 'posts'

urlpatterns = [
    # path('posts-api/', views.posts_list_api),
    # path('posts-detail-api/<int:pk>/', views.posts_detail_api),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
