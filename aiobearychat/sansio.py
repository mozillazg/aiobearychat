# -*- coding: utf-8 -*-
import json
from typing import Dict, Optional
from urllib.parse import urlencode

import attr


@attr.s
class Response:
    status: str = attr.ib()
    headers: Dict = attr.ib()
    body: bytes = attr.ib()

    def json(self):
        return json.loads(self.body)


def format_url(url, url_params: Optional[Dict] = None):
    if not url_params:
        return url
    return url + '?' + urlencode(url_params)


def clean_nothing_keys(origin_dict: Dict):
    """移除值为 NOTHING 的 key"""
    return {
        k: v
        for k, v in origin_dict.items()
        if k is not attr.NOTHING
    }
