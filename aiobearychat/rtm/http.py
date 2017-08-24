# -*- coding: utf-8 -*-
"""RTM HTTP 相关 API."""
from typing import Any, Optional

from attr import NOTHING

from aiobearychat.abc import API, Requester
from aiobearychat.sansio import Response, clean_nothing_keys


class RtmAPI(API):
    """RTM HTTP 相关 API.

    :param requester: 实际进行请求操作的 requester
    :type requester: aiobearychat.abc.Requester
    :param token: RTM token, 目前可以通过创建 hubot 机器人获得
    :type token: str
    :param base_url: RTM HTTP API
    :type base_url: str

    """

    #: RTM HTTP API 的基地址
    base_url = 'https://rtm.bearychat.com'  # type: str

    def __init__(self, requester: Requester, token: str = NOTHING, *,
                 base_url: str = ''):
        #: RTM HTTP API 的基地址
        self.base_url = base_url or self.base_url  # type: str
        self._token = token    # type: str
        super().__init__(requester=requester, token=self._token,
                         base_url=self.base_url)

    async def start(self, **requester_params: Any) -> Response:
        """获取 RTM 模式的连接地址和用户信息。

        官方文档地址：
        https://github.com/bearyinnovative/OpenAPI/blob/master/rtm/api_start.md

        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "code": 0,
                  "result": {
                    // RTM token 对应用户结构
                    "user": {},
                    // RTM 连接地址 5 分钟内有效
                    "ws_host": "wss://rtm.bearychat.com/nimbus/ws:xxx"
                  }
                }

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        url_params.update({
        })

        url = self.base_url + '/start'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        return await self._make_request('post',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)

    async def message(self, vchannel: str, text: str, *,
                      markdown: bool = True,
                      attachments: Optional[list] = None,
                      **requester_params: Any) -> Response:
        """发送富文本消息

        官方文档地址：
        https://github.com/bearyinnovative/OpenAPI/blob/master/rtm/api_message.md

        :param vchannel: 目标会话 id，示例：``=bw52O``
        :type vchannel: str
        :param text: 消息正文
        :type text: str
        :param markdown: 消息正文是否使用 markdown 格式？（默认值： ``True``)
        :type markdown: bool
        :param attachments: 消息 attachment 结构，示例:

                            ::

                                [
                                    {
                                      "title": "test_title",     # attachment 标题，title / text 至少包含一个
                                      "text": "test_text",       # attachment 内容，title / text 至少包含一个
                                      "images": [{               # attachment 图片列表，可选
                                        "url": "http://example.com/1.jpg"
                                      }],
                                      "color": "#cb3f20"        # attachment 颜色，可选
                                    }
                                ]

        :type attachments: :class:`list`

        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "code": 0,
                  "result": null
                }

        """  # noqa
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'vchannel': vchannel,
            'text': text,
            'markdown': markdown,
            'attachments': attachments or [],
        })

        url = self.base_url + '/message'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        return await self._make_request('post',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)
