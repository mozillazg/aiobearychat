====================================================================
 ``aiobearychat.openapi``
====================================================================

.. contents::
    :local:

.. currentmodule:: aiobearychat.openapi

.. automodule:: aiobearychat.openapi


    .. autoclass:: aiobearychat.openapi.OpenAPI

        :members:
        :undoc-members:

        .. attribute:: base_url

            开放 API 的基地址。 默认是 ``https://api.bearychat.com/v1``
        .. attribute:: meta

            meta 相关 API (是个 :class:`aiobearychat.openapi.meta_api.MetaAPI` 实例).
        .. attribute:: team

            团队相关 API (是个 :class:`aiobearychat.openapi.team_api.TeamAPI` 实例).
        .. attribute:: user

            用户相关 API (是个 :class:`aiobearychat.openapi.user_api.UserAPI` 实例).
        .. attribute:: vchannel

            聊天会话相关 API (是个 :class:`aiobearychat.openapi.vchannel_api.VchannelAPI` 实例).
        .. attribute:: channel

            讨论组相关 API (是个 :class:`aiobearychat.openapi.channel_api.ChannelAPI` 实例).
        .. attribute:: session_channel

            临时讨论组相关 API (是个 :class:`aiobearychat.openapi.session_channel_api.SessionChannelAPI` 实例).
        .. attribute:: p2p

            P2P 会话相关 API (是个 :class:`aiobearychat.openapi.p2p_api.P2pAPI` 实例).
        .. attribute:: message

            消息相关 API (是个 :class:`aiobearychat.openapi.message_api.MessageAPI` 实例).
        .. attribute:: emoji

            团队自定义 emoji 相关 API (是个 :class:`aiobearychat.openapi.emoji_api.EmojiAPI` 实例).
        .. attribute:: sticker

            团队 sticker 相关 API (是个 :class:`aiobearychat.openapi.sticker_api.StickerAPI` 实例).
        .. attribute:: rtm

            RTM 相关 API (是个 :class:`aiobearychat.openapi.rtm_api.RtmAPI` 实例).
