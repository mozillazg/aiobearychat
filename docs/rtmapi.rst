RTM 服务 HTTP API
=========================

使用示例
------------


.. code-block:: python

    import aiohttp

    from aiobearychat.rtm.aiohttp import RtmAPI


    async def main(token):
        async with aiohttp.ClientSession() as session:
            api = RtmAPI(session, token=token)
            response = await api.start()
            pprint(response.json())


上面的 :class:`aiobearychat.rtm.aiohttp.RtmAPI` 是 :class:`aiobearychat.rtm.RtmAPI` 的子类，表示使用
``aiohttp`` 这个模块来进行 http 请求相关的操作。

具体 api 可以查看
:class:`aiobearychat.rtm.RtmAPI` 的文档，同时也可以参考
`官方文档 <https://github.com/bearyinnovative/OpenAPI/blob/master/rtm/api.md>`__ 来理解
每个方法的含义。



可用的快捷封装
--------------

使用 aiohttp 进行 http 请求相关的操作:

* :class:`aiobearychat.rtm.aiohttp.RtmAPI`
