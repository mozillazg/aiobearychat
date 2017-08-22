# -*- coding: utf-8 -*-
"""讨论组相关 API.

auto generated by script at 2017-08-22 22:47:00.738298. don't edit it.

"""
from typing import Any

from attr import NOTHING

from aiobearychat.abc import API
from aiobearychat.sansio import Response, clean_nothing_keys


class ChannelAPI(API):
    """讨论组相关 API."""

    async def info(self,
                   channel_id: str,
                   **requester_params: Any) -> Response:
        """返回指定讨论组的完整信息。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.info.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

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

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
            'channel_id': channel_id,
        })

        url = self.base_url + '/channel.info'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        return await self._make_request('get',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)

    async def list(self,
                   **requester_params: Any) -> Response:
        """返回团队内的讨论组列表，获取某个讨论组的完整信息，请使用 ``channel.info``.

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.list.md



        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                [
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
                ]

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
        })

        url = self.base_url + '/channel.list'
        headers = {
            'content-type': 'application/json',
        }

        url_params = clean_nothing_keys(url_params)
        body_params = clean_nothing_keys(body_params)

        return await self._make_request('get',
                                        url,
                                        url_params=url_params,
                                        body_params=body_params,
                                        headers=headers,
                                        **requester_params)

    async def create(self,
                     name: str,
                     *,
                     topic: str = NOTHING,
                     private: bool = NOTHING,
                     **requester_params: Any) -> Response:
        """创建一个讨论组.

                官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.create.md



                :param name: | 讨论组名称，可以包含 2 到 20 个英文字符或 1 到 10 个中文字符。
        | 允许使用数字、下划线 (``_``)、中线 (``-``) 和点。 (示例: ``吃喝玩乐在深圳``)
                :type name: str


                :param topic: 讨论组话题 (示例: ``今天吃什么？``)
                :type topic: str


                :param private: 讨论组是否为私密？
                :type private: bool


                :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
                :rtype: :class:`aiobearychat.sansio.Response`

                ``response.body`` 返回值示例::

                    response.status 等于 201 时:

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

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'name': name,
            'topic': topic,
            'private': private,
        })
        url = self.base_url + '/channel.create'
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

    async def archive(self,
                      channel_id: str,
                      **requester_params: Any) -> Response:
        """归档一个讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.archive.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "private": false,
                  "general": true,
                  "latest_ts": 1486367046281,
                  "uid": "=bw52O",
                  "name": "所有人",
                  "is_member": false,
                  "is_active": false,
                  "type": "normal",
                  "topic": null,
                  "member_uids": [
                    "=bw52O"
                  ],
                  "vchannel_id": "=bw52O",
                  "id": "=bw52O",
                  "team_id": "=bw52O"
                }

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
        })
        url = self.base_url + '/channel.archive'
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

    async def unarchive(self,
                        channel_id: str,
                        **requester_params: Any) -> Response:
        """恢复一个已被归档的讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.unarchive.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

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

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
        })
        url = self.base_url + '/channel.unarchive'
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

    async def leave(self,
                    channel_id: str,
                    **requester_params: Any) -> Response:
        """当前用户离开讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.leave.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
        })
        url = self.base_url + '/channel.leave'
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

    async def join(self,
                   channel_id: str,
                   **requester_params: Any) -> Response:
        """当前用户加入指定讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.join.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "private": false,
                  "general": false,
                  "latest_ts": 1486367046281,
                  "uid": "=bw52O",
                  "name": "吃喝玩乐在深圳",
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

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
        })
        url = self.base_url + '/channel.join'
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

    async def invite(self,
                     channel_id: str,
                     invite_uid: str,
                     **requester_params: Any) -> Response:
        """当前用户邀请一个团队成员加入讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.invite.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :param invite_uid: 邀请用户 id (示例: ``=bw52O``)
        :type invite_uid: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
            'invite_uid': invite_uid,
        })
        url = self.base_url + '/channel.invite'
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

    async def kick(self,
                   channel_id: str,
                   kick_uid: str,
                   **requester_params: Any) -> Response:
        """当前用户移除一个讨论组成员。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.kick.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :param kick_uid: 移除用户 id (示例: ``=bw52O``)
        :type kick_uid: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
            'kick_uid': kick_uid,
        })
        url = self.base_url + '/channel.kick'
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

    async def kickout(self,
                      channel_id: str,
                      kick_uid: str,
                      **requester_params: Any) -> Response:
        """当前用户移除一个讨论组成员。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/channel.kickout.md



        :param channel_id: 讨论组 id (示例: ``=bw52O``)
        :type channel_id: str


        :param kick_uid: 移除用户 id (示例: ``=bw52O``)
        :type kick_uid: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'channel_id': channel_id,
            'kick_uid': kick_uid,
        })
        url = self.base_url + '/channel.kickout'
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
