from django.shortcuts import get_object_or_404
from django.views import generic
from django import http

from . import models


class KeeperView(generic.View):

    def get(self, request, path):
        keeper = get_object_or_404(models.Keeper, name=path)

        response_params = {"content": keeper.data}
        if keeper.content_type:
            response_params["content_type"] = keeper.content_type
        if keeper.charset:
            response_params["charset"] = keeper.charset
        if keeper.reason:
            response_params["reason"] = keeper.reason
        if keeper.status:
            response_params["status"] = keeper.status

        return http.HttpResponse(**response_params)

    def post(self, request, path):
        keeper = get_object_or_404(models.Keeper, name=path)
        if keeper.token and keeper.token != request.META.get("HTTP_X_TOKEN"):
            raise http.Http404()

        keeper.data = request.body
        keeper.reason = request.GET.get("reason")
        keeper.status = request.GET.get("status")
        keeper.charset = request.GET.get("charset")
        keeper.content_type = request.META.get("CONTENT_TYPE")
        keeper.save()
        return http.HttpResponse(
            keeper.data, reason=keeper.reason, charset=keeper.charset,
            status=keeper.status, content_type=keeper.content_type,
        )
