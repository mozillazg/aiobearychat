# -*- coding: utf-8 -*-
"""获取用户列表"""
import asyncio
import os
from pprint import pprint

import aiohttp

from aiobearychat.openapi.aiohttp import OpenAPI


async def main(token):
    async with aiohttp.ClientSession() as session:
        api = OpenAPI(session, token=token)
        response = await api.user.list()
        pprint(response.json())


if __name__ == '__main__':
    token = os.getenv('AIOBEARYCHAT_TOKEN')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(token))
    finally:
        loop.close()
