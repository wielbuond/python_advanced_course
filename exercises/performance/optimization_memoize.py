"""
* Assignment: Memoization
* Complexity: medium
* Lines of code: 5 lines
* Time: 13 min

English:

    X. Run doctests - all must succeed

Polish:
    1. Stwórz pusty `dict` o nazwie `CACHE`
    2. W słowniku będziemy przechowywali wyniki wyliczenia funkcji dla zadanych parametrów:
        a. klucz: argument funkcji
        b. wartość: wynik obliczeń
    3. Zmodyfikuj funkcję `factorial_cache(n: int)`
    4. Przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:
        a. jeżeli tak, to zwraca dane z `CACHE`
        b. jeżeli nie, to oblicza, aktualizuje `CACHE`, a następnie zwraca wartość
    5. Porównaj prędkość działania
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:

"""

from timeit import timeit
import sys
sys.setrecursionlimit(5000)


def factorial_cache(n: int) -> int:
    ...


# Do not modify anything below
def factorial_nocache(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_nocache(n - 1)


duration_cache = timeit(
    stmt='factorial_cache(500); factorial_cache(400); factorial_cache(450); factorial_cache(350)',
    globals=globals(),
    number=10000,
)

duration_nocache = timeit(
    stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
    globals=globals(),
    number=10000
)

print(f'factorial_cache time: {round(duration_cache, 4)} seconds')
print(f'factorial_nocache time: {round(duration_nocache, 3)} seconds')
print(f'Cached solution is {round(duration_nocache / duration_cache, 1)} times faster')
