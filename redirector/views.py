from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from . import models


class RedirectView(generic.View):

    def get(self, request, path):
        url_mapping = models.UrlMapping.objects.filter(alias=path).first()

        if url_mapping:
            url_mapping.visit()

            return redirect(url_mapping.raw_url, permanent=False)
        search_paths = path.rsplit("/")
        if search_paths:
            search_path = " ".join(search_paths)
        else:
            search_path = path
        suggestions = None
        if request.user.is_staff:
            for path in search_paths:
                qs = models.UrlMapping.objects.filter(alias__contains=path)
                if suggestions is None:
                    suggestions = qs
                else:
                    suggestions |= qs
        return render(request, "redirector/404.html", {
            "search_path": search_path,
            "suggestions": suggestions,
        })
