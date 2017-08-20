开放 API (OpenAPI) 服务
=========================

使用示例
------------


.. code-block:: python

    import aiohttp

    from aiobearychat.openapi.aiohttp import OpenAPI


    async def main(token):
        async with aiohttp.ClientSession() as session:
            api = OpenAPI(session, token=token)
            response = await api.user.list()
            print(response.json())



上面的 ``OpenAPI`` 是 :class:`aiobearychat.openapi.OpenAPI` 的子类，表示使用
``aiohttp`` 这个模块来进行 http 请求相关的操作。

具体 api 可以查看
:class:`aiobearychat.openapi.OpenAPI` 的文档，同时也可以参考
`官方文档 <https://github.com/bearyinnovative/OpenAPI/tree/master/api>`__ 来理解
每个方法的含义。
