# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

from aiobearychat.openapi.aiohttp import OpenAPI


def test_init():
    session = MagicMock()
    token = 'ttt'
    api = OpenAPI(session, token=token)
    assert api.meta._requester._session == session
    assert api._token == token
    assert api.meta._token == token
