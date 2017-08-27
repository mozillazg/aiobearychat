# -*- coding: utf-8 -*-
import json

import attr

from aiobearychat import sansio


def test_format_url_params_none():
    url = 'http://abc.com/efrf/'
    result = sansio.format_url(url, url_params=None)
    assert result == url


def test_format_url_params_dict():
    url = 'http://abc.com/efrf/'
    params = {
        'a': 'b',
        'c': 'd',
    }
    result = sansio.format_url(url, url_params=params)
    assert result == url + '?a=b&c=d'


def test_clean_nothing_keys():
    d = {
        'a': 'b',
        'c': attr.NOTHING,
    }
    result = sansio.clean_nothing_keys(d)
    assert 'c' not in result


def test_clean_nothing_keys_no_change():
    d = {
        1: 2,
        'a': 'b',
        'c': 'e',
    }
    result = sansio.clean_nothing_keys(d)
    assert result == d


def test_response_json():
    d = {
        'a': 2,
        'e': 3,
        'abc': '测试',
    }
    response = sansio.Response(200, {}, json.dumps(d))
    assert response.json() == d
