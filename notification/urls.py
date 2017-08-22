from django.conf.urls import include, url

import notification.views as views

urlpatterns = [
    url(r'^health$', views.HealthView.as_view(), name='health'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
