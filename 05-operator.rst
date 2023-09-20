

Operator String About
=====================
* ``str()``
* ``repr()``


Str
---
* ``print(obj)``
* ``f'{obj}'``
* ``f'{obj!s}'``
* ``str(obj)``
* ``obj.__str__()``


Repr
----
* ``obj``
* ``f'{obj!r}'``
* ``repr(obj)``
* ``obj.__repr__()``


Operator String Str
===================
* Calling ``print(obj)`` calls ``str(obj)``
* Calling ``str(obj)`` calls ``obj.__str__()``
* Method ``obj.__str__()`` must return ``str``
* Intended for end-users of your class


Inherited
---------


Overloaded
----------


Operator String Repr
====================
* Typing ``obj`` into REPL (console) calls ``repr(obj)``
* Calling ``repr(obj)`` calls ``obj.__repr__()``
* Method ``obj.__repr__()`` must return ``str``
* Intended for developers of your class
* Shows object representation
* Copy-paste for creating object with the same values
* Useful for debugging
* Printing ``list`` will call ``__repr__()`` method on each element


Inherited
---------


Overloaded
----------


Nested
------
* Printing ``list`` will call ``__repr__()`` method on each element


Operator String Format
======================
* Calling function ``format(obj, fmt)`` calls ``obj.__format__(fmt)``
* Method ``obj.__format__()`` must return ``str``
* Used for advanced formatting in f-strings (``f'...'``)


Operator String Operators
=========================
* ``+`` - add
* ``-`` - sub
* ``*`` - mul
* ``%`` - mod
* ``+=`` - iadd
* ``-=`` - isub
* ``*=`` - imul
* ``%=`` - imod


About
-----


Mod
---
* ``%`` (``__mod__``) operator behavior for ``int`` and ``str``:


Operator Arithmetic About
=========================
* Operator Overload
* Operator Overload is the Pythonic way
* Operator Overload allows readable syntax
* Operator Overload allows simpler operations
* All examples in this chapter uses ``dataclasses`` for you to focus on the important code, not boilerplate code just to make it works


Operators
---------
* Source: https://github.com/python/cpython/blob/main/Grammar/python.gram#L695
* Comparison: ``==``, ``!=``, ``<=``, ``<``, ``>=``, ``>``, ``not in``, ``in``, ``is not``, ``is``
* Bitwise: ``|``, ``^``, ``&``, ``<<``, ``>>``
* Arithmetic: ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``@``, ``**``, ``~``


Recap
-----


Problem
-------
* ``dataclass`` is used to generate ``__init__()`` and ``__repr__()``
* ``dataclass`` does not have any influence on addition


Solution
--------


Further Reading
---------------
* https://docs.python.org/reference/datamodel.html#emulating-numeric-types
* https://docs.python.org/library/operator.html


Operator Left
=============
* ``x + y`` - will call method "add" on object ``x`` (``x.__add__(y)``)
* ``x - y`` - will call method "sub" on object ``x`` (``x.__sub__(y)``)
* ``x * y`` - will call method "mul" on object ``x`` (``x.__mul__(y)``)
* ``x ** y`` - will call method "pow" on object ``x`` (``x.__pow__(y)``)
* ``x @ y`` - will call method "matmul" on object ``x`` (``x.__matmul__(y)``)
* ``x / y`` - will call method "truediv" on object ``x`` (``x.__truediv__(y)``)
* ``x // y`` - will call method "floordiv" on object ``x`` (``x.__floordiv__(y)``)
* ``x % y`` - will call method "mod" on object ``x`` (``x.__mod__(y)``)


Memory
------
* ``tuple`` is immutable
* ``list`` is mutable
* ``tuple + tuple`` will generate new ``tuple``
* ``list + list`` will generate new ``list``
* ``__add__()`` operator on ``tuple`` is the same as on ``list``


Operator Increment
==================
* ``x += y`` - will call method "iadd" on object ``x`` (``x.__iadd__(y)``)
* ``x -= y`` - will call method "isub" on object ``x`` (``x.__isub__(y)``)
* ``x *= y`` - will call method "imul" on object ``x`` (``x.__imul__(y)``)
* ``x **= y`` - will call method "ipow" on object ``x`` (``x.__ipow__(y)``)
* ``x @= y`` - will call method "imatmul" on object ``x`` (``x.__imatmul__(y)``)
* ``x /= y`` - will call method "itruediv" on object ``x`` (``x.__itruediv__(y)``)
* ``x //= y`` - will call method "ifloordiv" on object ``x`` (``x.__ifloordiv__(y)``)
* ``x %= y`` - will call method "imod" on object ``x`` (``x.__imod__(y)``)


Memory
------
* ``tuple`` is immutable
* ``list`` is mutable
* ``tuple += tuple`` will generate new ``tuple``
* ``list += list`` will update old ``list``
* ``__iadd__()`` operator on ``tuple`` is different than on ``list``


Syntax
------


Add vs Iadd
-----------


Operator Right
==============
* ``x + y`` - if method "add" on object ``x`` fails, then call "radd" on object ``y`` (``y.__radd__(x)``)
* ``x - y`` - if method "sub" on object ``x`` fails, then call "rsub" on object ``y`` (``y.__rsub__(x)``)
* ``x * y`` - if method "mul" on object ``x`` fails, then call "rmul" on object ``y`` (``y.__rmul__(x)``)
* ``x ** y`` - if method "pow" on object ``x`` fails, then call "rpow" on object ``y`` (``y.__rpow__(x)``)
* ``x @ y`` - if method "matmul" on object ``x`` fails, then call "rmatmul" on object ``y`` (``y.__rmatmul__(x)``)
* ``x / y`` - if method "truediv" on object ``x`` fails, then call "rtruediv" on object ``y`` (``y.__rtruediv__(x)``)
* ``x // y`` - if method "floordiv" on object ``x`` fails, then call "rfloordiv" on object ``y`` (``y.__rfloordiv__(x)``)
* ``x % y`` - if method "mod" on object ``x`` fails, then call "rmod" on object ``y`` (``y.__rmod__(x)``)


Syntax
------


Left Operation
--------------


Both
----


Operator Comparison
===================
* ``in`` - contains


About
-----


Object Equality
---------------
* When you compare objects with the same fields from two different classes
* Always remember to compare classes
* This way you avoid bug, when both has the same fields and values
* Eq Works at Both Sides


Operator Comparison
===================
* ``in`` - contains
* https://github.com/python/cpython/blob/main/Grammar/python.gram#L695


About
-----


Operator Contains
=================
* ``in`` - contains
* ``y in x`` - will call "contains" on object x (``x.__contains__(y)``)


Implementation
--------------


Operator Bitwise
================
* ``&`` - and
* ``|`` - or
* ``^`` - xor
* ``&=`` - iand
* ``|=`` - ior
* ``^=`` - ixor
* ``<<`` - lshift
* ``>>`` - rshift
* ``<<=`` - ilshift
* ``>>=`` - irshift


About
-----


AND - Conjunction
-----------------


OR - Alternative
----------------


XOR - Exclusive Alternative
---------------------------


Bool
----


Set
---


Dict
----


Dictionary Update
-----------------


Operator Builtin
================
* ``abs()``
* ``bool()``
* ``complex()``
* ``del()``
* ``delattr()``
* ``dir()``
* ``divmod()``
* ``float()``
* ``getattr()``
* ``hash()``
* ``hex()``
* ``int()``
* ``iter()``
* ``len()``
* ``next()``
* ``oct()``
* ``pow()``
* ``reversed()``
* ``round()``
* ``setattr()``


About
-----


Length
------


Float
-----


Abs
---


Round
-----


Operator Accessors
==================
* ``obj(x)`` - call
* ``obj[x]`` - getitem
* ``obj[x]`` - missing
* ``obj[x] = 10`` - setitem
* ``del obj[x]`` - delitem


About
-----


Operator Reflection
===================
* When accessing an attribute
* ``setattr(obj, attrname, value) -> None``
* ``delattr(obj, attrname) -> None``
* ``getattr(obj, attrname, default) -> Any``
* ``hasattr(obj, attrname) -> bool``
* ``__setattr__(self, attrname, value) -> None``
* ``__delattr__(self, attrname) -> None``
* ``__getattribute__(self, attrname) -> Any``
* ``__getattr__(self, attrname) -> Any``


Problem
-------


Set Attribute
-------------
* Called when trying to set attribute to a value
* Typing ``obj.attrname = value``
* Will call ``setattr(obj, attrname, value)``
* Which triggers ``obj.__setattr__(attrname, value)``


Delete Attribute
----------------
* Called when trying to delete attribute
* Typing ``del obj.attrname``
* Will call ``delattr(obj, attrname)``
* Which triggers ``mark.__delattr__(name)``


Get Attribute If Exists
-----------------------
* Called for every time, when you want to access any attribute
* Before even checking if this attribute exists
* If attribute is not found, then raises ``AttributeError`` and calls ``__getattr__()``
* Typing ``obj.attrname``
* Will call ``getattr(obj, attrname)``
* Which triggers ``obj.__getattribute__(attrname)``
* If ok: then return value
* If error: then call ``obj.__getattr__(attrname)``


Get Attribute If Missing
------------------------
* Called whenever you request an attribute that hasn't already been defined
* It will not execute, when attribute already exist
* Implementing a fallback for missing attributes


Has Attribute
-------------
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calling ``hasattr(obj, attrname)``
* Will call ``__getattribute__()`` and checks if raises ``AttributeError``
* If no exception, then return ``True``
* If exception, then call ``__getattr__()`` and check
* If ``__getattr__()`` succeeds then return ``True``
* If ``__getattr__()`` fail then return ``False``


Operator Numerical
==================
* ``-obj`` - neg
* ``+obj`` - pos
* ``~obj`` - invert


About
-----
