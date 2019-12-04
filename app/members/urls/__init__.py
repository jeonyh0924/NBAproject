from django.urls import path, include

from members.urls import form_code, apis_code
from .. import views

app_name = 'members'

urlpatterns = [
    path('', include(form_code)),
    path('api/', include(apis_code)),
]