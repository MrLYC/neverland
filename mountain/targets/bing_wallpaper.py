# encoding: utf-8

import requests
import urlparse

from mountain.targets import BaseTarget, http

from ycyc.base.iterutils import getitems


class BingWallPaperView(BaseTarget):
    base_url = "http://www.bing.com"

    def get(self):
        r = requests.get(
            urlparse.urljoin(
                self.base_url,
                "/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN",
            )
        )
        data = r.json()

        path = getitems(data, ["images", 0, "url"])

        if not path:
            return http.HttpResponseNotFound()

        r = requests.get(urlparse.urljoin(self.base_url, path))
        return http.HttpResponse(
            r.content,
            content_type=r.headers["Content-Type"],
        )
