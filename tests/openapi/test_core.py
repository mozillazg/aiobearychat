# -*- coding: utf-8 -*-
import pytest

from aiobearychat.openapi.core import OpenAPI


def test_init_openapi(requester):
    token = 'axxre'
    api = OpenAPI(requester, token=token)
    assert api._token == token
    assert api.meta._requester == requester


def test_init_openapi_base_url(requester):
    token = 'axxre'
    base_url = 'http://a.com/c'
    api = OpenAPI(requester, token=token, base_url=base_url)
    assert api.base_url == base_url
    assert api.meta.base_url == base_url


class TestOpenAPI:
    @pytest.yield_fixture(autouse=True)
    def setup_api(self, requester):
        self.token = 'tokenxxx'
        self.api = OpenAPI(requester, token=self.token)

    @pytest.mark.asyncio
    async def test_meta_get(self):
        await self.api.meta.get()
        requester = self.api.meta._requester
        request_params = requester.request_params
        assert request_params.method == 'get'
        assert request_params.url == self.api.base_url + '/meta'

    @pytest.mark.asyncio
    async def test_message_post(self):
        vchannel_id = 'atere_ere'
        text = '中文斥呵啥'
        attachments = []
        await self.api.message.create(vchannel_id, text, attachments)
        requester = self.api.meta._requester
        request_params = requester.request_params
        payload = request_params.body_deserialize()
        assert request_params.method == 'post'
        assert request_params.url == self.api.base_url + '/message.create'
        assert payload['token'] == self.token
        assert payload['vchannel_id'] == vchannel_id
        assert payload['attachments'] == attachments
