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

    def __init__(self, status: int, headers: Dict, body: bytes):
        super().__init__(status=status, headers=headers, body=body)

    def json(self) -> Any:
        """反序列化 ``body`` 的值"""
        return json.loads(self.body)


def format_url(url: str, url_params: Optional[Dict] = None) -> str:
    if not url_params:
        return url
    return url + '?' + urlencode(url_params)


def clean_nothing_keys(origin_dict: Dict) -> Dict:
    """移除 value 为 NOTHING 的 key"""
    return {
        key: value
        for key, value in origin_dict.items()
        if value is not attr.NOTHING
    }
