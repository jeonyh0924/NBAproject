from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import apis_code as views

# app_name = 'posts'

urlpatterns = [
    path('posts_api/', views.posts_list_api),
    path('posts_detail_api/<int:pk>/', views.posts_detail_api),
    path('api_postlist/', views.api_PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
