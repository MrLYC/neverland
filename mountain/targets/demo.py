# encoding: utf-8

from django.utils.timezone import now

from mountain.targets import BaseTarget


class DemoView(BaseTarget):
    def get(self):
        response = dict(self.request.GET)
        response["time"] = now()
        return response
