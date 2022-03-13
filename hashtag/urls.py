from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^hashtag/$', views.get_tag, name='get_hashtag'),
]