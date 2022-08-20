# aiothrottles

[![Licence](https://img.shields.io/badge/license-BSD-blue.svg)](https://github.com/KonstantinTogoi/aiothrottles/blob/master/LICENSE)
[![Last Release](https://img.shields.io/pypi/v/aiothrottles.svg)](https://pypi.python.org/pypi/aiothrottles)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/aiothrottles.svg)](https://pypi.python.org/pypi/aiothrottles)
[![Documentation](https://readthedocs.org/projects/aiothrottles/badge/?version=latest)](https://aiothrottles.readthedocs.io/en/latest/)

---

**Documentation**: https://aiothrottles.readthedocs.io/

**Source Code**: https://github.com/KonstantinTogoi/aiothrottles

---

aiothrottles synchronization primitives are designed to be extension to
[asyncio synchronization primitives](https://docs.python.org/3/library/asyncio-sync.html>).

## Usage

Throttle implements a rate limiting for asyncio task.
A throttle can be used to guarantee limited access to a shared resources.

The preferred way to use a Throttle is an
[async with](https://docs.python.org/3/reference/compound_stmts.html#async-with>)
statement:

```python
throttle = Throttle('3/s')

# ... later
async with throttle:
    # access shared state
```

which is equivalent to:

```python
throttle  = Throttle('3/s')

# ... later
await throttle.acquire()
try:
    # access shared state
finally:
    throttle.release()
```

A call rate is determined by the `rate` argument.
Pass the rate in the following formats:

- `"{integer limit}/{unit time}"`
- `"{limit's numerator}/{limit's denominator}{unit time}"`

`rate` examples:

- `4/s`, `5/m`, `6/h`, `7/d`
- `1/second`, `2/minute`, `3/hour`, `4/day`
- `1/3s`, `12/37m`, `1/5h`, `8/3d`

## Installation

```shell
pip install aiothrottles
```

or

```shell
python setup.py install
```

## Supported Python Versions

Python 3.6, 3.7, 3.8 and 3.9 are supported.
