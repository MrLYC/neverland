from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import models


class RedirectView(generic.View):
    def get(self, request, path):
        url_mapping = get_object_or_404(models.UrlMapping, alias=path)

        url_mapping.visit()

        return redirect(url_mapping.raw_url)
