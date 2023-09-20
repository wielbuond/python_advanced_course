"""
* Assignment: Protocol Descriptor Inheritance
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    1. Define class `GeographicCoordinate`
    2. Use descriptors to check value boundaries
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `GeographicCoordinate`
    2. Użyj deskryptory do sprawdzania wartości brzegowych
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> place1 = GeographicCoordinate(50, 120, 8000)
    >>> place1
    Latitude: 50, Longitude: 120, Elevation: 8000

    >>> place2 = GeographicCoordinate(22, 33, 44)
    >>> place2
    Latitude: 22, Longitude: 33, Elevation: 44

    >>> place1.latitude = 1
    >>> place1.longitude = 2
    >>> place1
    Latitude: 1, Longitude: 2, Elevation: 8000

    >>> place2
    Latitude: 22, Longitude: 33, Elevation: 44

    >>> GeographicCoordinate(90, 0, 0)
    Latitude: 90, Longitude: 0, Elevation: 0
    >>> GeographicCoordinate(-90, 0, 0)
    Latitude: -90, Longitude: 0, Elevation: 0
    >>> GeographicCoordinate(0, +180, 0)
    Latitude: 0, Longitude: 180, Elevation: 0
    >>> GeographicCoordinate(0, -180, 0)
    Latitude: 0, Longitude: -180, Elevation: 0
    >>> GeographicCoordinate(0, 0, +8848)
    Latitude: 0, Longitude: 0, Elevation: 8848
    >>> GeographicCoordinate(0, 0, -10994)
    Latitude: 0, Longitude: 0, Elevation: -10994

    >>> GeographicCoordinate(-91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(+91, 0, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, -181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, +181, 0)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, -10995)
    Traceback (most recent call last):
    ValueError: Out of bounds

    >>> GeographicCoordinate(0, 0, +8849)
    Traceback (most recent call last):
    ValueError: Out of bounds
"""

class GeographicCoordinate:
    def __str__(self):
        return f'Latitude: {self.latitude}, ' +\
               f'Longitude: {self.longitude}, ' +\
               f'Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()


"""
latitude - min: -90.0, max: 90.0
longitude - min: -180.0, max: 180.0
elevation - min: -10994.0, max: 8848.0
"""


