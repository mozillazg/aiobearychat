# -*- coding: utf-8 -*-
"""消息相关 API.

auto generated by script at 2017-08-24 21:50:13.459796. don't edit it.

"""
from typing import Any

from attr import NOTHING

from aiobearychat.abc import API
from aiobearychat.sansio import Response, clean_nothing_keys


class MessageAPI(API):
    """消息相关 API."""

    async def query(self,
                    vchannel_id: str,
                    query: str,
                    **requester_params: Any) -> Response:
        """查询指定 vchannel 下的消息列表。支持以下几种查询算法：

        ``latest``
        ~~~~~~~~~~

        查询 vchannel 下最新的消息，支持参数：

        -  ``limit``: 查询数量限制，最大值为 100, 默认 20

        ``since``
        ~~~~~~~~~

        从指定位置开始拉取若干条消息，支持参数：

        -  ``key``: 开始位置的消息 key, 不可以和 ``ts`` 同时使用
        -  ``ts``: 开始位置的消息 ts, 不可以和 ``ts`` 同时使用
        -  ``forward``: 向前（时间发生方向）获取条数
        -  ``backward``: 向后（时间发生方向）获取条数

        **注意**:

        #. 使用 ``key`` 查询时，查询区间不包括 key 对应的消息
        #. 使用 ``ts`` 查询时，查询区间包括 ts 对应的消息
        #. ``forward`` / ``backward`` 参数可以同时使用
        #. ``forward`` / ``backward`` 参数最大值为 100,
        #. ``forward`` / ``backward`` 均未指定时，默认使用 ``forward=100``

        ``window``
        ~~~~~~~~~~

        拉取一定时间窗口内的消息，支持参数：

        -  ``from_key`` / ``to_key``: 窗口区间的消息 key
        -  ``from_ts`` / ``to_ts``: 窗口区间的消息 ts
        -  ``forward``: 从 from 方向往 to 方向取的消息数
        -  ``backward``: 从 to 方向往 from 方向取的消息数

        **注意**:

        #. ``{from,to}_key`` 和 ``{from,to}_ts`` 不可以混用
        #. 使用 ``{from,to}_key`` 查询时，查询区间不包括 key 对应的消息
        #. 使用 ``{from,to}_ts`` 查询时，查询区间包括 ts 对应的消息
        #. ``forward`` 和 ``backward`` 参数只能选其中一个
        #. ``forward`` / ``backward`` 均未指定时，默认使用 ``forward=100``
        #. 如果查询区间开始值比结束值大，返回空结果

                官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/message.query.md



                :param vchannel_id: 待查询 vchannel\_id (示例: ``=bw52O``)
                :type vchannel_id: :class:`str`


                :param query: 消息查询 payload
                :type query: :class:`str`


                :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
                :rtype: :class:`aiobearychat.sansio.Response`

                ``response.body`` 返回值示例::

                    response.status 等于 200 时:

                        {
                          "messages": [
                            {
                              "key": "1485236262366.0193",
                              "updated": "2017-01-24T13:37:42.000+0000",
                              "is_channel": false,
                              "uid": "=bw52O",
                              "fallback": null,
                              "attachments": [],
                              "created": "2017-01-24T13:37:42.000+0000",
                              "vchannel_id": "=bw52O",
                              "refer_key": null,
                              "robot_id": null,
                              "created_ts": 1485236262366,
                              "team_id": "=bw52O",
                              "subtype": "normal",
                              "text": "hello"
                            }
                          ]
                        }

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'vchannel_id': vchannel_id,
            'query': query,
        })
        url = self.base_url + '/message.query'
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

    async def info(self,
                   vchannel_id: str,
                   message_key: str,
                   **requester_params: Any) -> Response:
        """返回一条消息的信息。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/message.info.md



        :param vchannel_id: 指定的目标聊天会话 id (示例: ``=bw52O``)
        :type vchannel_id: :class:`str`


        :param message_key: 获取消息的 key (示例: ``1487667236785.0077``)
        :type message_key: :class:`str`


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "key": "1485236262366.0193",
                  "updated": "2017-01-24T13:37:42.000+0000",
                  "is_channel": false,
                  "uid": "=bw52O",
                  "fallback": null,
                  "attachments": [],
                  "created": "2017-01-24T13:37:42.000+0000",
                  "vchannel_id": "=bw52O",
                  "refer_key": null,
                  "robot_id": null,
                  "created_ts": 1485236262366,
                  "team_id": "=bw52O",
                  "subtype": "normal",
                  "text": "hello"
                }

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
            'vchannel_id': vchannel_id,
            'message_key': message_key,
        })

        url = self.base_url + '/message.info'
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

    async def create(self,
                     vchannel_id: str,
                     text: str,
                     attachments: list,
                     **requester_params: Any) -> Response:
        """发送一条消息到指定聊天会话。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/message.create.md



        :param vchannel_id: 指定的目标聊天会话 id (示例: ``=bw52O``)
        :type vchannel_id: :class:`str`


        :param text: 消息内容 (示例: ``中午吃啥啊？``)
        :type text: :class:`str`


        :param attachments: 消息附件
        :type attachments: :class:`list`


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 201 时:

                {
                  "key": "1485236262366.0193",
                  "updated": "2017-01-24T13:37:42.000+0000",
                  "is_channel": false,
                  "uid": "=bw52O",
                  "fallback": null,
                  "attachments": [],
                  "created": "2017-01-24T13:37:42.000+0000",
                  "vchannel_id": "=bw52O",
                  "refer_key": null,
                  "robot_id": null,
                  "created_ts": 1485236262366,
                  "team_id": "=bw52O",
                  "subtype": "normal",
                  "text": "hello"
                }

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'vchannel_id': vchannel_id,
            'text': text,
            'attachments': attachments,
        })
        url = self.base_url + '/message.create'
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

    async def delete(self,
                     vchannel_id: str,
                     message_key: str,
                     **requester_params: Any) -> Response:
        """删除一条消息。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/message.delete.md



        :param vchannel_id: 消息聊天会话 id (示例: ``=bw52O``)
        :type vchannel_id: :class:`str`


        :param message_key: 删除的消息 key (示例: ``1487667236785.0077``)
        :type message_key: :class:`str`


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'vchannel_id': vchannel_id,
            'message_key': message_key,
        })
        url = self.base_url + '/message.delete'
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

    async def update_text(self,
                          vchannel_id: str,
                          message_key: str,
                          text: str,
                          **requester_params: Any) -> Response:
        """更新一条消息的内容。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/message.update_text.md



        :param vchannel_id: 消息聊天会话 id (示例: ``=bw52O``)
        :type vchannel_id: :class:`str`


        :param message_key: 更新的消息 key (示例: ``1487667236785.0077``)
        :type message_key: :class:`str`


        :param text: 更新的消息内容 (示例: ``中午吃啥啊？``)
        :type text: :class:`str`


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "key": "1485236262366.0193",
                  "updated": "2017-01-24T13:37:42.000+0000",
                  "is_channel": false,
                  "uid": "=bw52O",
                  "fallback": null,
                  "attachments": [],
                  "created": "2017-01-24T13:37:42.000+0000",
                  "vchannel_id": "=bw52O",
                  "refer_key": null,
                  "robot_id": null,
                  "created_ts": 1485236262366,
                  "team_id": "=bw52O",
                  "subtype": "normal",
                  "text": "hello"
                }

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'vchannel_id': vchannel_id,
            'message_key': message_key,
            'text': text,
        })
        url = self.base_url + '/message.update_text'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        return await self._make_request('patch',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)
