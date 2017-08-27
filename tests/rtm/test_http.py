# -*- coding: utf-8 -*-
import pytest

from aiobearychat.rtm.http import RtmAPI


class TestRtmAPI:

    @pytest.yield_fixture(autouse=True)
    def setup_api(self, requester):
        self.token = token = 'token'
        self.api = RtmAPI(requester, token=token)

    @pytest.mark.asyncio
    async def test_start(self):
        api = self.api
        await api.start()
        requester = api._requester
        request_params = requester.request_params

        url = request_params.url
        payload = request_params.body_deserialize()
        assert url == api.base_url + '/start'
        assert payload['token'] == self.token

    @pytest.mark.asyncio
    async def test_message(self):
        api = self.api
        vchannel = '=xxxabc'
        text = 'hello'
        await api.message(vchannel, text)
        requester = api._requester
        request_params = requester.request_params

        url = request_params.url
        payload = request_params.body_deserialize()
        assert url == api.base_url + '/message'
        assert payload['token'] == self.token
        assert payload['vchannel'] == vchannel
