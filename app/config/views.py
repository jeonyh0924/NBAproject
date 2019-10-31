from django.shortcuts import redirect, render

from posts.models import Post


def index(request):
    # return redirect('posts:post-list')
    post_list_queryset = Post.objects.all()
    post_list = []
    for post in post_list_queryset:
        post_list.append(post)

    for i in range(1, len(post_list)):
        for j in range(0, len(post_list) - 1):
            if post_list[j].like_users.count() < post_list[j + 1].like_users.count():
                post_list[j + 1], post_list[j] = post_list[j], post_list[j + 1]

    best_posts = post_list[0:3]
    context = {
        'best_posts': best_posts,
    }
    return render(request, 'base.html', context)
