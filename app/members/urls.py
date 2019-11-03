from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('', views.team_list, name='team-list'),
    path('<int:team_id>/', views.detail, name='team-detail'),
    path('player/<int:player_id>/', views.player_detail, name='player-detail'),
    path('challenge/', views.challenge, name='challenge'),
    path('challengeValid', views.challenge_valid, name='valid'),
    path('playervalid/<int:player_pk>/', views.player_valid, name='player-valid'),
    path('playerclear', views.player_clear, name='player-clear'),
]