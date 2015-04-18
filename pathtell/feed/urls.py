from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^feed$', 'feed.views.feed', name='feed'),
]
