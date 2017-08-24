# -*- coding: utf-8 -*-
import aiohttp
import attr

from aiobearychat.requesters.aiohttp import Requester
from aiobearychat import rtm


class RtmAPI(rtm.RtmAPI):
    """使用 aiohttp 作为 RtmAPI 中相关 API 的 HTTP 请求模块

    使用示例::

        async def main(token):
            async with aiohttp.ClientSession() as session:
                api = RtmAPI(session, token=token)
                response = await api.start()
                print(response.json())

    """
    def __init__(self, session: aiohttp.ClientSession,
                 token: str = attr.NOTHING, *,
                 base_url: str = ''):
        requester = Requester(session=session)  # type: Requester
        super().__init__(requester=requester, token=token, base_url=base_url)
