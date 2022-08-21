.. py:currentmodule:: aiothrottles

Examples
========

awaitable
---------

Use of :code:`aiothrottles.Throttle` as awaitable object:

    >>> import time
    >>> from aiothrottles import Throttle
    >>>
    >>> throttle = Throttle(rate='1/s')
    >>>
    >>> async def foo(n):
    ...     print(n, time.time())
    ...
    >>> for i in range(5):
    ...     await throttle
    ...     await foo(i)
    ...     throttle.release()
    ...
    0 1563275828.253736
    1 1563275829.2547996
    2 1563275830.2562528
    3 1563275831.257302
    4 1563275832.2587304

context manager
---------------

Use of :code:`aiothrottles.Throttle` as context:

    >>> import time
    >>> from aiothrottles import Throttle
    >>>
    >>> throttle = Throttle(rate='1/s')
    >>>
    >>> async def foo(n):
    ...     print(n, time.time())
    ...
    >>> for i in range(5):
    ...     async with throttle:
    ...         await foo(i)
    ...
    0 1563275898.6722345
    1 1563275899.673589
    2 1563275900.6750457
    3 1563275901.6763387
    4 1563275902.6777005

decorator
---------

Use of :code:`aiothrottles.Throttle` as decorator for coroutines:

    >>> import time
    >>> from aiothrottles import throttle  # Throttle alias
    >>>
    >>> @throttle(rate='1/s')
    ... async def foo(n):
    ...     print(n, time.time())
    ...
    >>> for i in range(5):
    ...     await foo(i)
    ...
    0 1563272100.4413373
    1 1563272101.4427333
    2 1563272102.4441307
    3 1563272103.445542
    4 1563272104.4468124
