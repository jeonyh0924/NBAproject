from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from members.models import Team, Player

# 팀 전체의 리스트를 보여준다.
from users.models import Challenge


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
        'type': f'test',
    }
    # return render(request, 'challenge/test_1.html', context)
    return render(request, 'challenge/test.html', context)


# 받아 온 선수가 challenge 양식에 맞는지
def challenge_valid(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('pk', None)
        player = Player.objects.get(pk=id)
        pass


# challenge player dollars option valid function
def player_valid(request, player_pk):
    # challenge 에 대한 정보
    pk = Player.objects.get(pk=player_pk)
    name = pk.name
    username = request.user.username
    value = int(request.GET.get('test'))

    # challenge 에 대한 정보를 render 시 내보낼 데이터들 views.challenge 와 같은 기능을 한다.
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
        'type': f'test',
    }
    change = int(15)

    if change >= 0:
        Challenge.objects.create(
            user=request.user,
            player=pk,
            type='test',
        )
        query_player_list = request.user.like_player.all()
        player_list = []
        for i in query_player_list:
            player_list.append(i.name)
            change -= int(i.playeroption.filter(type='test')[0].value)

        messages.info(request, f'선수 : {name} 는 ({username})의 선수가 되었습니다. 남은 dollars는 {change}')
        messages.info(request, f'사용자의 선수들은 {player_list} 입니다')
        return render(request, 'challenge/test.html', context)


def player_clear(request):
    request.user.like_player.clear()
    return redirect('members:challenge')
