# encoding: utf-8
import logging

from django.shortcuts import get_object_or_404
from django import http

from mountain.models import ViewRule
from mountain.register import Targets

logger = logging.getLogger(__name__)


def target_view(request, path):
    rule = get_object_or_404(ViewRule, path=path, method=request.method)

    if rule.token and request.GET.get("tk") != rule.token:
        return http.HttpResponseForbidden()

    target_cls = Targets.get(rule.target)
    if not target_cls:
        return http.HttpResponseNotFound("target %s not found" % rule.target)

    try:
        target = target_cls(rule, request, path)
        return target.handle()
    except Exception as err:
        logger.exception(err)
        return http.HttpResponseServerError()
