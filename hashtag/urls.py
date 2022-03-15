from django.urls import re_path
from . import views

app_name="hashtag"
urlpatterns = [
    re_path('hashtag', views.get_tag, name='get_hashtag'),
    re_path('news', views.get_news, name='get_news'),
]