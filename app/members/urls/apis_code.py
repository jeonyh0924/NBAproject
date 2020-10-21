from django.urls import path

from .. import apis as views

urlpatterns = [
    path('player/', views.PlayerList.as_view()),
    path('player/<int:pk>/', views.PlayerDetail.as_view()),
    path('', views.TeamList.as_view()),
    path('<int:pk>/', views.TeamDetail.as_view()),
]
