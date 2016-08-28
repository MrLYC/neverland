from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<path>[\w/\-]+)/?$', views.target_view),
]
