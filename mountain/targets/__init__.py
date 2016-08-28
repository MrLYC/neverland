# encoding: utf-8

import six

from django import http


class BaseTargetMeta(type):
    def __new__(cls, name, bases, attrs):
        target_name = attrs.get("name") or name
        target_description = attrs.get("description") or target_name
        attrs["name"] = target_name
        attrs["description"] = target_description

        return type.__new__(cls, name, bases, attrs)


class BaseTarget(six.with_metaclass(BaseTargetMeta, object)):
    description = None
    name = None

    def __init__(self, rule, request, path):
        self.rule = rule
        self.request = request
        self.path = path

    def default_handle(self):
        return http.HttpResponseNotAllowed()

    get = default_handle
    post = default_handle
    put = default_handle
    patch = default_handle
    delete = default_handle

    def handle(self):
        method = self.request.method.lower()

        handler = getattr(self, method, self.default_handle)
        response = handler()

        if isinstance(response, http.response.HttpResponseBase):
            return response

        elif isinstance(response, basestring):
            return http.HttpResponse(content=response)

        else:
            return http.JsonResponse(response)
