# encoding: utf-8

import requests

from mountain.targets import BaseTarget, http

from ycyc.base.iterutils import getitems


class BingWallPaperView(BaseTarget):
    def get(self):
        r = requests.get(
            "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
        )
        data = r.json()

        url = getitems(data, ["images", 0, "url"])

        if not url:
            return http.HttpResponseNotFound()

        r = requests.get(url)
        return http.HttpResponse(
            r.content,
            content_type=r.headers["Content-Type"],
        )
