"""
* Assignment: Operator String Nested
* Required: yes
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Overload `str` and `repr` to achieve desired printing output
    2. Run doctests - all must succeed

Polish:
    1. Przeciąż `str` i `repr` aby osiągnąć oczekiwany rezultat wypisywania
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Define `Accounts.__str__()`
    * Define `User.__str__()` and `User.__repr__()`
    * Define `Group.__repr__()`
    * Printing list will call repr on all elements

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = User('Rick', 'Martinez')
    >>> print(result)
    Rick Martinez

    >>> result = User('Mark', 'Watney', groups=[
    ...     Group(gid=2, name='staff'),
    ... ])
    >>> print(result)
    Mark Watney member of [gid=2(staff)]

    >>> result = User('Melissa', 'Lewis', groups=[
    ...     Group(gid=1, name='admins'),
    ...     Group(gid=2, name='staff'),
    ... ])
    >>> print(result)
    Melissa Lewis member of [gid=1(admins), gid=2(staff)]

    >>> result = Accounts([
    ...     User('Mark', 'Watney', groups=[
    ...         Group(gid=2, name='staff'),
    ...     ]),
    ...     User('Melissa', 'Lewis', groups=[
    ...         Group(gid=1, name='admins'),
    ...         Group(gid=2, name='staff'),
    ...     ]),
    ...     User('Rick', 'Martinez'),
    ... ])
    >>>
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    Mark Watney member of [gid=2(staff)]
    Melissa Lewis member of [gid=1(admins), gid=2(staff)]
    Rick Martinez
"""


class Accounts:
    def __init__(self, users):
        self.users = users


class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups else []


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name


