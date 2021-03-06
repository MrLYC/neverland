from django.shortcuts import get_object_or_404
from django.views import generic
from django import http
from django.conf import settings

from . import models


class KeeperView(generic.View):

    def get(self, request, path):
        keeper = get_object_or_404(models.Keeper, name=path)
        read_token = keeper.read_token
        if read_token and read_token != request.GET.get("read_token"):
            return http.HttpResponseNotFound()

        response_params = {
            "content": keeper.data,
            "charset": keeper.charset or None,
        }
        if keeper.content_type:
            response_params["content_type"] = keeper.content_type
        if keeper.reason:
            response_params["reason"] = keeper.reason
        if keeper.status:
            response_params["status"] = keeper.status

        keeper.visit()

        return http.HttpResponse(**response_params)

    def post(self, request, path):
        keeper = get_object_or_404(models.Keeper, name=path)
        write_token = request.META.get("HTTP_WRITE_TOKEN")
        if keeper.write_token and keeper.write_token != write_token:
            raise http.Http404()

        keeper.data = request.body

        write_token = request.META.get("HTTP_NEWWRITE_TOKEN")
        if write_token is not None:
            keeper.write_token = write_token

        read_token = request.META.get("HTTP_READ_TOKEN")
        if read_token is not None:
            keeper.read_token = read_token

        reason = request.GET.get("reason")
        if reason is not None:
            keeper.reason = reason

        status = request.GET.get("status")
        if status is not None:
            keeper.status = status

        charset = request.GET.get("charset", request.encoding)
        keeper.charset = charset

        content_type = request.META.get("CONTENT_TYPE")
        if content_type is not None:
            keeper.c_type = content_type.split(";")[0]

        keeper.save()

        return http.HttpResponse(
            keeper.data, reason=keeper.reason, charset=keeper.charset or None,
            status=keeper.status, content_type=keeper.content_type,
        )
