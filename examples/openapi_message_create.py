# -*- coding: utf-8 -*-
"""向会话发送消息"""
import asyncio
import os
from pprint import pprint

import aiohttp

from aiobearychat.openapi.aiohttp import OpenAPI


async def main(token):
    async with aiohttp.ClientSession() as session:
        api = OpenAPI(session, token=token)
        response = await api.channel.list()
        pprint(response.json())
        vchannel_id = response.json()[0]['vchannel_id']
        response = await api.message.create(vchannel_id, 'hello test sdk', [])
        pprint(response.json())


if __name__ == '__main__':
    token = os.getenv('AIOBEARYCHAT_TOKEN')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(token))
    finally:
        loop.close()
