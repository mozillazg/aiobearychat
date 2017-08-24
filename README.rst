===============================
aiobearychat
===============================

.. image:: https://img.shields.io/pypi/v/aiobearychat.svg
        :target: https://pypi.python.org/pypi/aiobearychat

.. image:: https://img.shields.io/travis/mozillazg/aiobearychat.svg
        :target: https://travis-ci.org/mozillazg/aiobearychat

.. image:: https://img.shields.io/coveralls/mozillazg/aiobearychat/master.svg
        :target: https://coveralls.io/r/mozillazg/aiobearychat

.. image:: https://readthedocs.org/projects/aiobearychat/badge/?version=latest
        :target: https://readthedocs.org/projects/aiobearychat/?badge=latest
        :alt: Documentation Status

.. image:: https://badges.gitter.im/mozillazg/aiobearychat.svg
        :alt: Join the chat at https://gitter.im/mozillazg/aiobearychat
        :target: https://gitter.im/mozillazg/aiobearychat



An async `BearyChat <https://bearychat.com/>`_ API library for Python

* Free software: MIT license
* Documentation: https://aiobearychat.readthedocs.org
* GitHub: https://github.com/mozillazg/aiobearychat
* PyPI: https://pypi.python.org/pypi/aiobearychat
* Python version: 3.5, 3.6

Features
--------

* `BearyChat <https://bearychat.com/>`_ 异步 I/O Python SDK
* 支持不同的异步 I/O HTTP 请求模块（aiohttp, tornado, ...)
* 封装所有的 OpenAPI
* 封装所有的 RTM HTTP API


Installation
------------

At the command line::

    $ pip install aiobearychat[aiohttp]


Usage
-----


OpenAPI
~~~~~~~

.. code-block:: python

    import aiohttp

    from aiobearychat.openapi.aiohttp import OpenAPI


    async def main(token):
        async with aiohttp.ClientSession() as session:
            api = OpenAPI(session, token=token)
            response = await api.user.list()
            print(response.json())


RTM HTTP API
~~~~~~~~~~~~

.. code-block:: python

    import aiohttp

    from aiobearychat.rtm.aiohttp import RtmAPI


    async def main(token):
        async with aiohttp.ClientSession() as session:
            api = RtmAPI(session, token=token)
            response = await api.start()
            pprint(response.json())


Credits
-------

This package was created with Cookiecutter_ and the `mozillazg/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`mozillazg/cookiecutter-pypackage`: https://github.com/mozillazg/cookiecutter-pypackage
