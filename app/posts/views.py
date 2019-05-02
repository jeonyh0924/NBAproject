from django.shortcuts import render, redirect

from users.models import User
from .models import Post
from .forms import PostCreateForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('posts:post-list')

    if request.method == 'POST':
        post = Post(
            user=request.user,
            image=request.FILES['photo'],
        )
        post.save()
        return redirect('posts:post-list')
    else:
        form = PostCreateForm()

        context = {
            'form': form,
        }
        return render(request, 'posts/post_create.html', context)
