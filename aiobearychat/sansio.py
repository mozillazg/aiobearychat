# -*- coding: utf-8 -*-
import json
from typing import Dict, Optional, Any
from urllib.parse import urlencode

import attr


@attr.s
class Response:
    """请求响应信息"""
    #: 状态码，比如 200
    status = attr.ib()  # type: int
    headers = attr.ib()  # type: Dict
    body = attr.ib()  # type: bytes

    def json(self) -> Any:
        """反序列化 ``body`` 的值"""
        return json.loads(self.body)


def format_url(url: str, url_params: Optional[Dict] = None) -> str:
    if not url_params:
        return url
    return url + '?' + urlencode(url_params)


def clean_nothing_keys(origin_dict: Dict) -> Dict:
    """移除值为 NOTHING 的 key"""
    return {
        k: v
        for k, v in origin_dict.items()
        if k is not attr.NOTHING
    }
