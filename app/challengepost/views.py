from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from challengepost.forms import challengeCommentForm, challengeCreateForm
from challengepost.models import challengePost


def post_list(request):
    posts = challengePost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'challenge/post_list.html', context)


def post_detail(request, post_pk):
    # 게시글의 작성자가 가진 선수들을 가져온다.
    chpost = challengePost.objects.get(pk=post_pk)
    player_query = chpost.author.like_player.all()
    player_list = []
    for player in player_query:
        player_list.append(player)

    post = challengePost.objects.get(pk=post_pk)
    # team_list = request.user.like_player.all()
    # create user의 team list를 저장 시킨 뒤, detail에서 보여주어야 한다.
    context = {
        'post': post,
        'comments_form': challengeCommentForm(),
        'player_list': player_list,
    }
    return render(request, 'challenge/post_detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('challengepost:list')
    if request.method == 'POST':
        form = challengeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(author=request.user)
            return redirect('challengepost:list')
    else:
        form = challengeCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'challenge/challengepost_create.html', context)


def comment_create(request, post_pk):
    if request.method == 'POST':
        post = challengePost.objects.get(pk=post_pk)
        form = challengeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('challengepost:detail', post_pk)


def post_like_toggle(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(challengePost, pk=post_pk)
        post.like_toggle(request.user)
        return redirect('challengepost:list')
