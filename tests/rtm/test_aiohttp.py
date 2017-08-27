# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

from aiobearychat.rtm.aiohttp import RtmAPI


def test_init():
    session = MagicMock()
    token = 'ttt'
    api = RtmAPI(session, token=token)
    assert api._requester._session == session
    assert api._token == token
