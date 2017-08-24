# -*- coding: utf-8 -*-
"""获取 BearyChat API 的状态"""
import asyncio
from pprint import pprint

import aiohttp

from aiobearychat.openapi.aiohttp import OpenAPI


async def main():
    async with aiohttp.ClientSession() as session:
        api = OpenAPI(session)
        response = await api.meta.get()
        pprint(response.json())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
