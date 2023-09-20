"""
* Assignment: Performance Compexity UniqueKeys
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Collect unique keys from all rows in one sequence `result`
    2. Run doctests - all must succeed

Polish:
    1. Zbierz unikalne klucze z wszystkich wierszy w jednej sekwencji `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `row.keys()`
    * Compare solutions with :ref:`Micro-benchmarking use case`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result is not Ellipsis
    True
    >>> type(result) in (set, list, tuple, frozenset)
    True
    >>> sorted(result)
    ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species']
"""

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

# Unique keys from DATA dicts
# type: set[str]
result = ...

