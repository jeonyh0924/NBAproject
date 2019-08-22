import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Post, Comment, HashTags
from .forms import PostCreateForm, CommentForm, PostForm


# Create your views here.
def post_list(request):
    # posts = Post.objects.all()
    # context = {
    #     'posts': posts,
    #     'comment_form': CommentForm(),
    # }
    # return render(request, 'posts/post_list.html', context)
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_base.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
        'comment_form': CommentForm(),
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    # if not request.user.is_authenticated:
    #     return redirect('users:login')

    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Post 모델은 공백을 허용한 부분을 제외하고는 채워져야 한다.
            # 그래서 form.save()를 동작시키는 순간에, 모델을 저장을 시킨다.
            # 그래서 메모리에 인스턴스로 post 변수를 만든 뒤
            # 유저에 대한 정보를 넣어주고, 저장한다.
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post-list')
            # 위에서 생성한, Post에 연결되는 Comment 생
            # if not form.cleaned_data['comment']:
            #     pass
            # else:
            #     comment_content = form.cleaned_data['comment']
            #     post.comments.create(
            #         author=request.user,
            #         content=comment_content,
            #     )

    else:
        form = PostForm()

    context['form'] = form
    return render(request, 'posts/post_create.html', context)


def comment_create(request, post_pk):
    # 1. post_pk 해당하는 Post 객체를 가져와  post 변수에 할당
    # 2. request.POST 에 전달 된 'content'키의 값을 content 변수에 할당
    # 3. Comment생성
    #   author : 현재 요청의 유저
    #   post : post_pk에 해당하는 Post객체
    #   content : request.POST로 전달 된 'content'키의 값
    # 4. posts:post-list로 redirect
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            return redirect('posts:post-detail', post_pk)
        # posts.forms.CommentCreateForm()을 사용
        # HTML 에서는 사용을 하지 않음

        # form = CommentForm(request.POST)
        # if form.is_valid():
        #   form.save(author= request.user, post=post)

        # content = request.POST['content']


def tag_post_list(request, tag_name):
    # Post중, 자신에게 속한 Comment가 가진 HashTag 목록 중 tag_name 이 name인 HashTag가 포함 된
    # Post 목록을 posts 변수에 할당
    # context 에 담아서 리턴 render
    # HTML: /posts/tag_post_list.html

    posts = Post.objects.filter(comments__tags__name=tag_name).distinct() | \
            Post.objects.filter(postTags__name=tag_name).distinct()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/tag_post_list.html', context)


def tag_search(request):
    # request.GET 으로 전달 된
    # search_keyword 값을 적절히 활용해서
    # 위의 tag_post_list view로 redirect
    # URL : '/posts/tag-search/'
    # URL Name : 'posts:tag-search'
    # teamplate는 음
    search_keyword = request.GET.get('search_keyword')
    substituted_keyword = re.sub(r'#|\s+', '', search_keyword)
    return redirect('posts:tag-post-list', substituted_keyword)
    # url = f'/posts/explore/tags/{search_keyword}/'
    # return redirect(url)


def post_like_toggle(request, post_pk):
    # URL: '/posts/<post_pk>/like-toggle/
    # URL Name: 'posts:post-like-toggle'
    # POST method
    # request.user가 post_pk에 해당하는 Post에
    #  Like Toggle처리
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        post.like_toggle(request.user)
        url = reverse('posts:post-list')
        return redirect(url + f'#post-{post_pk}')
