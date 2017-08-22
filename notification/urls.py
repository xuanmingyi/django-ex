from django.conf.urls import include, url

from notification.views import index, health

urlpatterns = [
    url(r'^health$', health),
    url(r'^$', index),
]
