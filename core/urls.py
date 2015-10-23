from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<path>[\w/\-]+)/?$', views.RedirectView.as_view()),
]
