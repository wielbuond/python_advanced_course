"""
* Assignment: OOP ObjectRelations HasPosition
* Complexity: easy
* Lines of code: 18 lines
* Time: 8 min

English:
    1. Define class `Point`
    2. Class `Point` has attributes `x: int = 0` and `y: int = 0`
    3. Define class `HasPosition`
    4. In `HasPosition` define method `get_position(self) -> Point`
    5. In `HasPosition` define method `set_position(self, x: int, y: int) -> None`
    6. In `HasPosition` define method `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
    7. Assume left-top screen corner as a initial coordinates position:
        a. going right add to `x`
        b. going left subtract from `x`
        c. going up subtract from `y`
        d. going down add to `y`
    8. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point`
    2. Klasa `Point` ma atrybuty `x: int = 0` oraz `y: int = 0`
    3. Zdefiniuj klasę `HasPosition`
    4. W `HasPosition` zdefiniuj metodę `get_position(self) -> Point`
    5. W `HasPosition` zdefiniuj metodę `set_position(self, x: int, y: int) -> None`
    6. W `HasPosition` zdefiniuj metodę `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
    7. Przyjmij górny lewy róg ekranu za punkt początkowy:
        a. idąc w prawo dodajesz `x`
        b. idąc w lewo odejmujesz `x`
        c. idąc w górę odejmujesz `y`
        d. idąc w dół dodajesz `y`
    8. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Point)
    >>> assert isclass(HasPosition)
    >>> assert hasattr(Point, 'x')
    >>> assert hasattr(Point, 'y')
    >>> assert hasattr(HasPosition, 'get_position')
    >>> assert hasattr(HasPosition, 'set_position')
    >>> assert hasattr(HasPosition, 'change_position')
    >>> assert ismethod(HasPosition().get_position)
    >>> assert ismethod(HasPosition().set_position)
    >>> assert ismethod(HasPosition().change_position)

    >>> class User(HasPosition):
    ...     pass

    >>> mark = User()

    >>> mark.set_position(x=1, y=2)
    >>> mark.get_position()
    Point(x=1, y=2)

    >>> mark.set_position(x=1, y=1)
    >>> mark.change_position(right=1)
    >>> mark.get_position()
    Point(x=2, y=1)

    >>> mark.set_position(x=1, y=1)
    >>> mark.change_position(left=1)
    >>> mark.get_position()
    Point(x=0, y=1)

    >>> mark.set_position(x=1, y=1)
    >>> mark.change_position(down=1)
    >>> mark.get_position()
    Point(x=1, y=2)

    >>> mark.set_position(x=1, y=1)
    >>> mark.change_position(up=1)
    >>> mark.get_position()
    Point(x=1, y=0)
"""

from dataclasses import dataclass, field


@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class HasPosition:
    _position: Point = field(default_factory=Point)

    def set_position(self, x: int, y: int) -> None:
        self._position = Point(x, y)

    def get_position(self) -> Point:
        return self._position

    def change_position(self, left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0) -> None:
        current = self.get_position()
        new_x = current.x + right - left
        new_y = current.y - up + down
        self.set_position(new_x, new_y)
