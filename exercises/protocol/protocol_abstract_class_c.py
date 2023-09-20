"""
* Assignment: OOP AbstractClass Typing
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Modify abstract class `Account`
    2. Add type annotation to all methods and attributes
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę abstrakcyjną `Account`
    2. Dodaj anotację typów do wszystkich metod i atrybutów
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isabstract, isclass, ismethod, signature

    >>> assert isclass(Account)
    >>> assert isabstract(Account)
    >>> assert hasattr(Account, '__init__')
    >>> assert hasattr(Account, 'login')
    >>> assert hasattr(Account, 'logout')
    >>> assert hasattr(Account.__init__, '__isabstractmethod__')
    >>> assert hasattr(Account.login, '__isabstractmethod__')
    >>> assert hasattr(Account.logout, '__isabstractmethod__')
    >>> assert Account.__init__.__isabstractmethod__ == True
    >>> assert Account.login.__isabstractmethod__ == True
    >>> assert Account.logout.__isabstractmethod__ == True

    >>> Account.__annotations__
    {'username': <class 'str'>, 'password': <class 'str'>}

    >>> Account.__init__.__annotations__
    {'username': <class 'str'>, 'password': <class 'str'>, 'return': None}

    >>> Account.login.__annotations__
    {'return': None}

    >>> Account.logout.__annotations__
    {'return': None}
"""


from abc import ABC, abstractmethod


# Modify class to add type annotation to all methods and attributes
class Account(ABC):
    username: str
    password: str

    @abstractmethod
    def __init__(self, username: str, password: str) -> None:
        ...

    @abstractmethod
    def login(self) -> None:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...


