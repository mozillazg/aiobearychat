# -*- coding: utf-8 -*-
"""临时讨论组相关 API.

auto generated by script at 2017-08-22 22:47:00.738298. don't edit it.

"""
from typing import Any

from attr import NOTHING

from aiobearychat.abc import API
from aiobearychat.sansio import Response, clean_nothing_keys


class SessionChannelAPI(API):
    """临时讨论组相关 API."""

    async def info(self,
                   session_channel_id: str,
                   **requester_params: Any) -> Response:
        """返回一个临时讨论组的完整信息。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.info.md



        :param session_channel_id: 讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

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

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
            'session_channel_id': session_channel_id,
        })

        url = self.base_url + '/session_channel.info'
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
        """| 返回团队内已经加入的临时讨论组列表，获取某个临时讨论组的完整信息，

        | 请使用 ``session_channel.info``.

                官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.list.md



                :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
                :rtype: :class:`aiobearychat.sansio.Response`

                ``response.body`` 返回值示例::

                    response.status 等于 200 时:

                        [
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
                        ]

        """
        url_params = {}
        body_params = {}
        url_params['token'] = self._token

        url_params.update({
        })

        url = self.base_url + '/session_channel.list'
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
                     member_uids: list,
                     *,
                     name: str = NOTHING,
                     **requester_params: Any) -> Response:
        """创建一个临时讨论组。

                官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.create.md



                :param name: | 临时讨论组名称，可以包含 2 到 20 个英文字符或 1 到 10 个中文字符。
        | 允许使用数字、下划线 (``_``)、中线 (``-``) 和点。 (示例: ``吃喝玩乐在深圳``)
                :type name: str


                :param member_uids: 临时讨论组成员 id 列表 (示例: ``["=bw52O", "=bw52P"]``)
                :type member_uids: list


                :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
                :rtype: :class:`aiobearychat.sansio.Response`

                ``response.body`` 返回值示例::

                    response.status 等于 201 时:

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

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'name': name,
            'member_uids': member_uids,
        })
        url = self.base_url + '/session_channel.create'
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
                      session_channel_id: str,
                      **requester_params: Any) -> Response:
        """归档一个临时讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.archive.md



        :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 200 时:

                {
                  "latest_ts": "1489242467694",
                  "name": "临时讨论组名称",
                  "is_member": true,
                  "is_active": false,
                  "type": "session",
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
            'session_channel_id': session_channel_id,
        })
        url = self.base_url + '/session_channel.archive'
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

    async def convert_to_channel(self,
                                 session_channel_id: str,
                                 name: str,
                                 *,
                                 private: bool = True,
                                 **requester_params: Any) -> Response:
        """将临时讨论组转换为讨论组。

                官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.convert_to_channel.md



                :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
                :type session_channel_id: str


                :param name: | 讨论组名称，可以包含 2 到 20 个英文字符或 1 到 10 个中文字符。
        | 允许使用数字、下划线 (``_``)、中线 (``-``) 和点。 (示例: ``吃喝玩乐在深圳``)
                :type name: str


                :param private: 讨论组是否为私密？默认值: ``True``
                :type private: bool


                :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
                :rtype: :class:`aiobearychat.sansio.Response`

                ``response.body`` 返回值示例::

                    response.status 等于 201 时:

                        {
                          "latest_ts": "1489242467694",
                          "name": "临时讨论组名称",
                          "is_member": true,
                          "is_active": false,
                          "type": "session",
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
            'session_channel_id': session_channel_id,
            'name': name,
            'private': private,
        })
        url = self.base_url + '/session_channel.convert_to_channel'
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
                    session_channel_id: str,
                    **requester_params: Any) -> Response:
        """离开临时讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.leave.md



        :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


        :return: response. 一个 :class:`aiobearychat.sansio.Response` 实例
        :rtype: :class:`aiobearychat.sansio.Response`

        ``response.body`` 返回值示例::

            response.status 等于 204 时:

        """
        url_params = {}
        body_params = {}
        body_params['token'] = self._token
        body_params.update({
            'session_channel_id': session_channel_id,
        })
        url = self.base_url + '/session_channel.leave'
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
                     session_channel_id: str,
                     invite_uid: str,
                     **requester_params: Any) -> Response:
        """邀请一个团队成员加入临时讨论组。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.invite.md



        :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


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
            'session_channel_id': session_channel_id,
            'invite_uid': invite_uid,
        })
        url = self.base_url + '/session_channel.invite'
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
                   session_channel_id: str,
                   kick_uid: str,
                   **requester_params: Any) -> Response:
        """移除一个临时讨论组成员。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.kick.md



        :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


        :param kick_uid: 邀请用户 id (示例: ``=bw52O``)
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
            'session_channel_id': session_channel_id,
            'kick_uid': kick_uid,
        })
        url = self.base_url + '/session_channel.kick'
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
                      session_channel_id: str,
                      kick_uid: str,
                      **requester_params: Any) -> Response:
        """移除一个临时讨论组成员。

        官方文档地址：https://github.com/bearyinnovative/OpenAPI/blob/master/api/session_channel.kickout.md



        :param session_channel_id: 临时讨论组 id (示例: ``=bw52O``)
        :type session_channel_id: str


        :param kick_uid: 邀请用户 id (示例: ``=bw52O``)
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
            'session_channel_id': session_channel_id,
            'kick_uid': kick_uid,
        })
        url = self.base_url + '/session_channel.kickout'
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
