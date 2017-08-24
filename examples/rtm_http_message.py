# -*- coding: utf-8 -*-
"""发送富文本消息"""
import asyncio
import os
from pprint import pprint

import aiohttp

from aiobearychat.openapi.aiohttp import OpenAPI
from aiobearychat.rtm.aiohttp import RtmAPI


async def main(token):
    async with aiohttp.ClientSession() as session:
        openapi = OpenAPI(session, token=token)
        response = await openapi.channel.list()
        vchannel_id = response.json()[0]['vchannel_id']

        api = RtmAPI(session, token=token)
        response = await api.message(
            vchannel_id, '''
# test

你好呀

```
print('hello world')
```

hello
''',
            markdown=True,
            attachments=[
                {
                    'title': 'test_title',
                    'text': 'test_text',
                    'images': [{
                        'url': 'https://avatars1.githubusercontent.com/u/485054?v=4&s=460'  # noqa
                    }],
                    'color': '#cb3f20'
                }
            ]
        )
        pprint(response.json())


if __name__ == '__main__':
    token = os.getenv('AIOBEARYCHAT_TOKEN')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(token))
    finally:
        loop.close()
