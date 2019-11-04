from django.shortcuts import redirect, render

from members.models import Player
from posts.models import Post


def index(request):
    # 인기글 best_posts
    post_list_queryset = Post.objects.all()
    post_list = []
    for post in post_list_queryset:
        post_list.append(post)

    for i in range(1, len(post_list)):
        for j in range(0, len(post_list) - 1):
            if post_list[j].like_users.count() < post_list[j + 1].like_users.count():
                post_list[j + 1], post_list[j] = post_list[j], post_list[j + 1]

    best_posts = post_list[0:3]

    # best_player
    best_player = Player.objects.first()
    player_query = Player.objects.all()
    player_list = []

    for player in player_query:
        player_list.append(player)

    for player in player_list:
        if int(player.like_users.count()) > int(best_player.like_users.count()):
            best_player = player

    context = {
        'best_posts': best_posts,
        'best_player': best_player,
    }
    return render(request, 'base.html', context)
