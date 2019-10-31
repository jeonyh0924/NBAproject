from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from members.models import Team, Player


# 팀 전체의 리스트를 보여준다.
def team_list(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'members/team_list.html', context)


# 특정 팀 페이지
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


# 특정 선수 페이지
def player_detail(request, player_id):
    teams = Team.objects.all()
    player = Player.objects.get(pk=player_id)
    context = {
        'teams': teams,
        'player': player,
    }
    return render(request, 'members/player_detail.html', context)


# 팀 맞추기
def challenge(request):
    player = []
    option_list = []
    player_all = Player.objects.all()

    for i in player_all:
        if i.playeroption.exists():
            player.append(i)

    for i in player:
        s = i.playeroption.filter(type='test')
        option_list.append(s[0].value)

    zip_list = zip(player, option_list)
    context = {
        'zip_lists': zip_list,
    }
    return render(request, 'challenge/test_1.html', context)
    # return render(request, 'challenge/test.html', context)


# 받아 온 선수가 challenge 양식에 맞는지
def challenge_valid(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk')
    pass

