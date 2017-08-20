# -*- coding: utf-8 -*-
import aiohttp
import attr

from aiobearychat.requesters.aiohttp import Requester
from aiobearychat import openapi


class OpenAPI(openapi.OpenAPI):
    def __init__(self, session: aiohttp.ClientSession,
                 token: str = attr.NOTHING, *,
                 base_url: str = ''):
        requester = Requester(session=session)
        super().__init__(requester=requester, token=token, base_url=base_url)
