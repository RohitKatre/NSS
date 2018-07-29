from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^register/$', UserCreateView.as_view(), name="create_user"),
]
