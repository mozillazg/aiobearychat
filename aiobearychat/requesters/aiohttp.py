# -*- coding: utf-8 -*-
import asyncio
from typing import Dict, Optional, Any

import aiohttp

from aiobearychat import abc
from aiobearychat.sansio import Response


class Requester(abc.Requester):
    def __init__(self, session: aiohttp.ClientSession, *args: Any,
                 **kwargs: Any) -> None:
        self._session = session
        super().__init__(*args, **kwargs)

    async def request(self, method: str, url: str,
                      body: bytes = b'', headers: Optional[Dict] = None,
                      **requester_params: Any) -> Response:
        async with self._session.request(
            method, url, headers=headers, data=body, **requester_params
        ) as response:
            return Response(
                status=response.status,
                headers=response.headers,
                body=await response.read(),
            )

    async def sleep(self, seconds: float) -> None:
        await asyncio.sleep(seconds)
