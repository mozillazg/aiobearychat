# -*- coding: utf-8 -*-
"""聊天会话相关 API.

auto generated by script at 2017-08-24 21:50:13.459796. don't edit it.

"""
from typing import Any

from attr import NOTHING

from aiobearychat.abc import API
from aiobearychat.sansio import Response, clean_nothing_keys


class VchannelAPI(API):
    """聊天会话相关 API."""

    async def info(self,
                   vchannel_id: str,
                   **requester_params: Any) -> Response:
        """返回指定聊天会话的完整信息。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/vchannel.info.md



        :param vchannel_id: 聊天会话 id (示例: ``=bw52O``)
        :type vchannel_id: :class:`str`


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                // Channel
                {
                  "private": false,
                  "general": true,
                  "latest_ts": 1486367046281,
                  "uid": "=bw52O",
                  "name": "所有人",
                  "is_member": false,
                  "is_active": true,
                  "type": "normal",
                  "topic": null,
                  "member_uids": [
                    "=bw52O"
                  ],
                  "vchannel_id": "=bw52O",
                  "id": "=bw52O",
                  "team_id": "=bw52O"
                }

                // SessionChannel
                {
                  "latest_ts": "1489242467694",
                  "name": "临时讨论组名称",
                  "is_member": true,
                  "is_active": true,
                  "type": "session",
                  "member_uids": [
                    "=bw52O"
                  ],
                  "vchannel_id": "=bw52O",
                  "id": "=bw52O",
                  "team_id": "=bw52O"
                }

                // P2PChannel
                {
                  "id": "=bw52O",
                  "team_id": "=bw52O",
                  "vchannel_id": "=bw52O",
                  "type": "p2p",
                  "is_active": true,
                  "is_member": true,
                  "member_uids": [
                    "=bw52O",
                    "=bw52P"
                  ],
                  "latest_ts": 1485238998284
                }

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
            'vchannel_id': vchannel_id,
        })

        url = self.base_url + '/vchannel.info'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        body_params = None

        return await self._make_request('get',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)
