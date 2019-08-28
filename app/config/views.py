from django.shortcuts import redirect, render


def index(request):
    # return redirect('posts:post-list')
    context = {

    }
    return render(request, 'base.html', context)
