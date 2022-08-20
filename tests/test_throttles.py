"""Tests."""
import time

import pytest
from aiothrottles import Throttle


class TestAwaitableMixin:
    """Tests of AwaitableMixin class."""

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_await_with_high_rate(self, high_rate):
        """Test high rates."""
        await self._test_await(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_await_with_mean_rate(self, mean_rate):
        """Test mean rates."""
        await self._test_await(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_await_with_low_rate(self, low_rate):
        """Test low rates."""
        await self._test_await(throttle=Throttle(low_rate), repeat=2)

    @staticmethod  # noqa: WPS602
    async def _test_await(throttle, repeat):
        """Test."""
        checkpoint = time.time() - throttle.period

        for iternum in range(repeat):
            await throttle
            if iternum % throttle.limit.numerator == 0:  # noqa: S001
                now = time.time()
                assert now - checkpoint >= throttle.period
                checkpoint = now
            throttle.release()


class TestContextManagerMixin:
    """Tests of ContetManagerMixin class."""

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_context_with_high_rate(self, high_rate):
        """Test high rates."""
        await self._test_context(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_context_with_mean_rate(self, mean_rate):
        """Test mean rates."""
        await self._test_context(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_context_with_low_rate(self, low_rate):
        """Test low rates."""
        await self._test_context(throttle=Throttle(low_rate), repeat=2)

    @pytest.mark.asyncio
    async def _test_context(self, throttle, repeat):
        """Test."""
        checkpoint = time.time() - throttle.period

        for iternum in range(repeat):
            async with throttle:
                if iternum % throttle.limit.numerator == 0:  # noqa: S001
                    now = time.time()
                    assert now - checkpoint >= throttle.period
                    checkpoint = now


class TestDecoratorMixin:
    """Tests of DecoratorMixin class."""

    @pytest.mark.asyncio
    @pytest.mark.high_rate
    async def test_decorator_with_high_rate(self, high_rate):
        """Test high rates."""
        await self._test_decorator(throttle=Throttle(high_rate), repeat=10)

    @pytest.mark.asyncio
    @pytest.mark.mean_rate
    async def test_decorator_with_mean_rate(self, mean_rate):
        """Test mean rates."""
        await self._test_decorator(throttle=Throttle(mean_rate), repeat=3)

    @pytest.mark.asyncio
    @pytest.mark.low_rate
    async def test_decorator_with_low_rate(self, low_rate):
        """Test low rates."""
        await self._test_decorator(throttle=Throttle(low_rate), repeat=2)

    @pytest.mark.asyncio
    async def _test_decorator(self, throttle: Throttle, repeat: int):
        """Test."""
        checkpoint = time.time() - throttle.period

        @throttle  # noqa: WPS430
        async def coroutine():
            pass  # noqa: WPS420

        for iternum in range(repeat):
            await coroutine()
            if iternum % throttle.limit.numerator == 0:  # noqa: S001
                now = time.time()
                assert now - checkpoint >= throttle.period
                checkpoint = now
