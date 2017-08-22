from django.conf.urls import include, url

from notification.views import index

urlpatterns = [
    url(r'^$', index),
]
