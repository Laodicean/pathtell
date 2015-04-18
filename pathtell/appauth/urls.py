from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'appauth.views.home', name='appauth_home'),
    url(r'^register$', 'appauth.views.register_view', name='appauth_register'),
    url(r'^login$', 'appauth.views.login_view', name='appauth_login'),
    url(r'^logout$', 'appauth.views.logout_view', name='appauth_logout'),
]
