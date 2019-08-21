from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.team_list, name='team-list'),
    path('<int:team_id>/', views.detail, name='team-detail'),
    path('player/<int:player_id>/', views.player_detail, name='player-detail'),
]
