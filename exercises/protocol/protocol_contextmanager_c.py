"""
* Assignment: Protocol Context Manager AutoSave
* Complexity: hard
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Modify class `File`
    2. Add class configuration attribute `AUTOSAVE_SECONDS: float = 1.0`
    3. Save buffer content to file every `AUTOSAVE_SECONDS` seconds
    4. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `File`
    2. Dodaj klasowy atrybut konfiguracyjny `AUTOSAVE_SECONDS: float = 1.0`
    3. Zapisuj zawartość bufora do pliku co `AUTOSAVE_SECONDS` sekund
    4. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
    5. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `from threading import Timer`
    * `timer = Timer(interval, function)`
    * `timer.start()`
    * `timer.cancel()`
    * `ctrl+c` or stop button kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> from inspect import isclass, ismethod
    >>> from time import sleep

    >>> assert isclass(File)
    >>> assert hasattr(File, 'append')
    >>> assert hasattr(File, 'AUTOSAVE_SECONDS')
    >>> assert hasattr(File, '__enter__')
    >>> assert hasattr(File, '__exit__')
    >>> assert ismethod(File(None).append)
    >>> assert ismethod(File(None).__enter__)
    >>> assert ismethod(File(None).__exit__)
    >>> assert File.AUTOSAVE_SECONDS == 1.0

    >>> with File('_temporary.txt') as file:
    ...     file.append('One')
    ...     file.append('Two')
    ...     sleep(1.0)
    ...     file.append('Three')
    ...     file.append('Four')
    ...     sleep(2.0)
    ...     file.append('Five')
    ...     file.append('Six')

    >>> open('_temporary.txt').read()
    'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'

    >>> remove('_temporary.txt')
"""

from threading import Timer


class File:
    ...


