"""
* Assignment: OOP Async Sleep
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define:
        a. coroutine function `a()`
    2. After running coroutine should:
        a. wait for 1.0 seconds
        b. return 'a'
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. coroutine function `a()`
    2. Po uruchomieniu coroutine powinna:
        a. czekać 1.0 sekundę
        b. zwracać 'a'
    3. Uruchom doctesty - wszystkie muszą się powieść

    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import iscoroutine, iscoroutinefunction
    >>> import asyncio

    >>> assert iscoroutinefunction(a)
    >>> assert iscoroutine(a())

    >>> asyncio.run(a())
    'a'
"""

import asyncio

# coroutine function `a()`
# wait for 1.0 seconds, return 'a'
# type: Coroutine
def a():
    ...

