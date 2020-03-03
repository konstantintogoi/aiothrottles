import time

import pytest

from aiothrottles import Throttle


class TestAwaitableMixin:

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_await_with_high_rate(self, high_rate):
        await self._test_await(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_await_with_mean_rate(self, mean_rate):
        await self._test_await(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_await_with_low_rate(self, low_rate):
        await self._test_await(throttle=Throttle(low_rate), repeat=2)

    @staticmethod
    async def _test_await(throttle, repeat):
        checkpoint = time.time() - throttle.period

        for i in range(repeat):
            await throttle
            if i % throttle.limit.numerator == 0:
                now = time.time()
                assert now - checkpoint >= throttle.period
                checkpoint = now
            throttle.release()


class TestContextManagerMixin:

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_context_with_high_rate(self, high_rate):
        await self._test_context(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_context_with_mean_rate(self, mean_rate):
        await self._test_context(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_context_with_low_rate(self, low_rate):
        await self._test_context(throttle=Throttle(low_rate), repeat=2)

    @pytest.mark.asyncio
    async def _test_context(self, throttle, repeat):
        checkpoint = time.time() - throttle.period

        for i in range(repeat):
            async with throttle:
                if i % throttle.limit.numerator == 0:
                    now = time.time()
                    assert now - checkpoint >= throttle.period
                    checkpoint = now


class TestWrapper:

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_wrapper_with_high_rate(self, high_rate):
        await self._test_wrapper(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_wrapper_with_mean_rate(self, mean_rate):
        await self._test_wrapper(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_wrapper_with_low_rate(self, low_rate):
        await self._test_wrapper(throttle=Throttle(low_rate), repeat=2)

    @pytest.mark.asyncio
    async def _test_wrapper(self, throttle, repeat):
        checkpoint = time.time() - throttle.period

        @throttle
        async def coroutine():
            pass

        for i in range(repeat):
            await coroutine()
            if i % throttle.limit.numerator == 0:
                now = time.time()
                assert now - checkpoint >= throttle.period
                checkpoint = now
