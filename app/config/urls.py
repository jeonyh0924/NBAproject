"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

from . import views
from posts.views import tag_post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    # /posts/ 로 들어오는 url 처리

    # path('', RedirectView.as_view(pattern_name='posts:post-list'), name='index'), 아래 문장과 성능은 동일하며
    # 위의 코드는 아래의 views.index로 갈 필요가 없다.
    path('', views.index, name='index'),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('members/', include('members.urls')),
    # path('explore/tags/<str:tag_name>/', tag_post_list, name='tag-post-list'),
    # 이미 존재하는 url
    path('accounts/', include('allauth.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),

]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
