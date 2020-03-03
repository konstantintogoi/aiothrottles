import pytest

from aiothrottles import Throttle


@pytest.fixture(params=[
    '2/s', '24/8s', '96/32s', '512/128s',
    '6/s', '21/3s', '80/10s', '999/111s',
])
def high_rate(request):
    return request.param


@pytest.fixture(params=['1/s', '3/3s', '15/15s', '123/123s'])
def mean_rate(request):
    return request.param


@pytest.fixture(params=[
    '1/2s', '8/24s', '32/96s', '512/128s',
    '1/6s', '3/21s', '10/80s', '999/111s',
])
def low_rate(request):
    return request.param


@pytest.fixture
def throttle(rate):
    return Throttle(rate)
