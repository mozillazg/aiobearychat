# -*- coding: utf-8 -*-
"""获取 RTM 模式的连接地址和用户信息"""
import asyncio
import os
from pprint import pprint

import aiohttp

from aiobearychat.rtm.aiohttp import RtmAPI


async def main(token):
    async with aiohttp.ClientSession() as session:
        api = RtmAPI(session, token=token)
        response = await api.start()
        pprint(response.json())


if __name__ == '__main__':
    token = os.getenv('AIOBEARYCHAT_TOKEN')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(token))
    finally:
        loop.close()
