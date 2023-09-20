"""
* Assignment: OOP AbstractInterface Values
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Define class `Setosa` implementing `IrisInterface`
    2. Implement methods
    3. Note, that attribute `species` is a `str`, and in Python you cannot add `str` and `float`
    4. Create protected method `_get_values()` which returns values of `int` and `float` type attibutes
    5. Why this method is not in interface?
    6. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Setosa` implementującą `IrisInterface`
    2. Zaimplementuj metody
    3. Zwróć uwagę, że atrybut `species` jest `str`, a Python nie można dodawać `str` i `float`
    4. Stwórz metodę chronioną `_get_values()`, która zwraca wartości atrybutów typu `int` i `float`
    5. Dlaczego ta metoda nie jest w interfejsie?
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `var(self).values()`
    * `instanceof()` or `type()`
    * `mean = sum() / len()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert issubclass(Setosa, IrisInterface)
    >>> assert hasattr(Setosa, 'mean')
    >>> assert hasattr(Setosa, 'sum')
    >>> assert hasattr(Setosa, 'len')

    >>> assert isfunction(Setosa.mean)
    >>> assert isfunction(Setosa.sum)
    >>> assert isfunction(Setosa.len)

    >>> Setosa.__annotations__  # doctest: +NORMALIZE_WHITESPACE
    {'sepal_length': <class 'float'>,
     'sepal_width': <class 'float'>,
     'petal_length': <class 'float'>,
     'petal_width': <class 'float'>,
     'species': <class 'str'>}

    >>> setosa = Setosa(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> setosa.len()
    4
    >>> setosa.sum()
    10.2
    >>> setosa.mean()
    2.55
"""

class IrisInterface:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float,
                 species: str,
                 ) -> None:
        raise NotImplementedError

    def mean(self) -> float:
        raise NotImplementedError

    def sum(self) -> float:
        raise NotImplementedError

    def len(self) -> int:
        raise NotImplementedError


