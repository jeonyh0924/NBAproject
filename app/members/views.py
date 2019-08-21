from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from members.models import Team, Player


def team_list(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'members/team_list.html', context)


def detail(request, team_id):
    teams = Team.objects.all()
    detail_team = Team.objects.get(pk=team_id)
    players = detail_team.player_set.all()
    context = {
        'teams': teams,
        'team': detail_team,
        'players': players,
    }
    return render(request, 'members/team_detail.html', context)


def player_detail(request, player_id):
    teams = Team.objects.all()
    player = Player.objects.get(pk=player_id)
    context = {
        'teams': teams,
        'player': player,
    }
    return render(request, 'members/player_detail.html', context)
