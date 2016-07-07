from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from . import models


class RedirectView(generic.View):

    def get(self, request, path):
        url_mapping = models.UrlMapping.objects.filter(alias=path).first()

        if not url_mapping:
            search_path = path.rsplit("/")[:-1]
            if search_path:
                search_path = " ".join(search_path)
            else:
                search_path = path
            return render(request, "redirector/404.html", dictionary={
                "search_path": search_path,
            })

        url_mapping.visit()

        return redirect(url_mapping.raw_url)
