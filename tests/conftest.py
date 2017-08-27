# -*- coding: utf-8 -*-
import asyncio
import json
from typing import Optional, Dict
from unittest.mock import MagicMock

import attr
import pytest

from aiobearychat.abc import Requester, Response


@attr.s
class RequestParams:
    method = attr.ib()
    url = attr.ib()
    body = attr.ib()
    headers = attr.ib()
    requester_params = attr.ib()

    def body_deserialize(self):
        return json.loads(self.body)


class MockRequester(Requester):
    def __init__(self, mock, response):
        self.mock = mock
        self.response = response
        self.request_params = None

    async def sleep(self, seconds: float) -> None:
        asyncio.sleep(0)
        self.mock.sleep(seconds)

    async def request(self, method: str, url: str, body: bytes = b'',
                      headers: Optional[Dict] = None,
                      **requester_params: Dict) -> Response:
        asyncio.sleep(0)
        self.request_params = RequestParams(
            method, url, body, headers,
            requester_params,
        )
        return self.response


@pytest.yield_fixture()
def requester():
    mock = MagicMock()
    response = MagicMock()

    yield MockRequester(mock, response)
