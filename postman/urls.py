# coding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<sender>[\w]+)/?$', views.MailToView.as_view()),
]
