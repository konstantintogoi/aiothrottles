# aiothrottles

[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/KonstantinTogoi/aiothrottles/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/aiothrottles.svg)](https://pypi.python.org/pypi/aiothrottles)
[![PyPI version](https://img.shields.io/pypi/pyversions/aiothrottles.svg)](https://pypi.python.org/pypi/aiothrottles)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://aiothrottles.readthedocs.io/en/latest/)
[![Travis status](https://travis-ci.org/KonstantinTogoi/aiothrottles.svg)](https://travis-ci.org/KonstantinTogoi/aiothrottles)

*aiothrottles* synchronization primitives are designed to be extension
(along the time) to *asyncio* synchronization primitives.

*aiothrottles* has the following basic synchronization primitives:

- `Throttle`

## Getting started

aiothrottles requires python 3.5+. Install package using pip

```python
pip install aiothrottles
```

### Throttle

Implements a rate limiting for asyncio task.
A throttle can be used to guarantee exclusive access to a shared resources
and locks access for a given time after releasing.

The preferred way to use a `Throttle` is an `async with` statement:

```python
throttle = Throttle('1/s')

# ... later
async with throttle:
    # access shared state
```

which is equivalent to:

```python
throttle  = Throttle('1/s')

# ... later
await throttle.acquire()
try:
    # access shared state
finally:
    throttle.release()
```

#### rates

The allowed call rate is determined by the `rate` argument.
Pass the rate in the format `{integer limit}/{unit time}` or
`{limit's numerator}/{limit's denominator}{unit time}`.
For, example:

- rates with integer limits
    + `4/s`, `5/m`, `6/h`, `7/d`
    + `1/second`, `2/minute`, `3/hour`, `4/day`
- rates with rational limits
    + `1/3s`, `12/37m`, `1/5h`, `8/3d`

## Examples

### decorator

Use of `Throttle` as decorator for coroutines:

```python
import time
from aiothrottles import throttle  # Throttle alias

@throttle(rate='1/s')
async def foo(n):
    print(n, time.time())

for i in range(5):
    await foo(i)

# 0 1563272100.4413373
# 1 1563272101.4427333
# 2 1563272102.4441307
# 3 1563272103.445542
# 4 1563272104.4468124
```

### awaitable

Use of `aiothrottles.Throttle` as awaitable object:

```python
import time
from aiothrottles import Throttle

throttle = Throttle(rate='1/s')

async def foo(n):
    print(n, time.time())

for i in range(5):
    await throttle
    await foo(i)

# 0 1563275828.253736
# 1 1563275829.2547996
# 2 1563275830.2562528
# 3 1563275831.257302
# 4 1563275832.2587304
```

### context manager

Use of `aiothrottles.Throttle` as context:

```python
import time
from aiothrottles import Throttle

throttle = Throttle(rate='1/s')

async def foo(n):
    print(n, time.time())

for i in range(5):
    async with throttle:
        await foo(i)

# 0 1563275898.6722345
# 1 1563275899.673589
# 2 1563275900.6750457
# 3 1563275901.6763387
# 4 1563275902.6777005
```

## License

**aiothrottles** is released under the BSD 3-Clause License.
