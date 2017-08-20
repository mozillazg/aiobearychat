# -*- coding: utf-8 -*-
import abc as _abc
import json
from typing import Dict, Optional, Any

from aiobearychat.sansio import Response, format_url


class Requester(_abc.ABC):

    def __init__(self, *args, **kwargs):
        pass

    @_abc.abstractmethod
    async def request(self, method: str, url: str,
                      body: bytes = b'', headers: Optional[Dict] = None,
                      **requester_params: Dict) -> Response:
        pass

    @_abc.abstractmethod
    async def sleep(self, seconds: float) -> None:
        pass


class API(_abc.ABC):
    def __init__(self, requester: Requester, token: str, *,
                 base_url: str, **kwargs):
        self._requester = requester
        self._token = token
        self.base_url = base_url

    async def _make_request(self, method: str, url: str, *,
                            url_params: Optional[Dict] = None,
                            body_params: Optional[Dict] = None,
                            headers: Optional[Dict] = None,
                            body: bytes = b'',
                            **requester_params: Any) -> Response:
        filled_url = format_url(url, url_params)

        if body_params is not None:
            body = json.dumps(body_params)

        response = await self._requester.request(
            method, filled_url, body, headers, **requester_params
        )
        return response
