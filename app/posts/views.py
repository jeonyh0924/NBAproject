from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Post, Comment
from .forms import PostCreateForm, CommentForm, PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'comment_form': CommentForm(),
    }
    return render(request, 'posts/post_list.html', context)


@login_required
def post_create(request):
    # if not request.user.is_authenticated:
    #     return redirect('users:login')

    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post-list')
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

            return redirect('posts:post-list')
        # posts.forms.CommentCreateForm()을 사용
        # HTML 에서는 사용을 하지 않음

        # form = CommentForm(request.POST)
        # if form.is_valid():
        #   form.save(author= request.user, post=post)

        # content = request.POST['content']

