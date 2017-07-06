from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<path>.+?)/?$', views.KeeperView.as_view()),
]
