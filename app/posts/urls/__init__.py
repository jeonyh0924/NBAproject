from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from posts.urls import apis_code, forms_code

app_name = 'posts'

urlpatterns = [
    path('apis/', include(apis_code)),
    path('forms/', include(forms_code)),
]
