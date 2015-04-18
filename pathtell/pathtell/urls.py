from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^', include('feed.urls')),
    url(r'^', include('landing.urls')),
    url(r'^auth/', include('appauth.urls')),
    url(r'^service/', include('services.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
