# -*- coding: utf-8 -*-

"""
test_aiobearychat
----------------------------------

Tests for `aiobearychat` module.
"""

import pytest

from aiobearychat import openapi  # noqa


@pytest.yield_fixture
def hello():
    # ...
    foo = 'hello'
    yield foo
    # ...


class TestAiobearychat:

    def test_000_something(self):
        pass
