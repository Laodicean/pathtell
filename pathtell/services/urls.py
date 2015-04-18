from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^add/$', 'services.views.person_add_service_view', name='person_add_service'),
]
