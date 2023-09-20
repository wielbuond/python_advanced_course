

Typing Basic
============
* Also known as: "type annotations", "type hints", "gradual typing"
* Types are not required, and never will be
* Good IDE will give you hints
* Types are used extensively in system libraries
* More and more books and documentations use types
* Introduced in Python 3.5
* Since Python 3.5: :pep:`484` -- Type Hints
* Since Python 3.6: :pep:`526` -- Syntax for Variable Annotations
* Since Python 3.8: :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* To type check use: ``mypy``, ``pyre-check``, ``pytypes``


Int
---
* Used to inform static type checker that the variable should be int


Float
-----
* Used to inform static type checker that the variable should be float


Str
---
* Used to inform static type checker that the variable should be str


Bool
----
* Used to inform static type checker that the variable should be bool


None
----
* Used to inform static type checker that the variable should be None


Errors
------
* Types are not Enforced
* This code will run without any problems
* Types are not required, and never will be
* Although ``mypy``, ``pyre-check`` or ``pytypes`` will throw error


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


Typing Annotations
==================


Alias
-----
* Used to make types more readable


Union
-----
* Used to inform static type checker that the variable should either X or Y
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y
* ``int | str == str | int``


Optional
--------
* Used to inform static type checker that the variable should be X or None
* ``int | None == None | int``


Final
-----
* Used to inform static type checker the value should not change
* Used to define constants
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal


Any
---


Further Reading
---------------
* More information in `cicd-tools`
* https://www.infoq.com/presentations/dynamic-static-typing/
* https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505


Typing Iterable
===============
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Tuple
-----


List
----


Set
---


Frozenset
---------


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing Mapping
==============
* Before Python 3.9 you need ``from typing import Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Dict
----


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing Nested
=============
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


List of Lists
-------------


List of Tuples
--------------


List of Dicts
-------------


Aliases
-------


Unions
------


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing TypedDict
================
* Since Python 3.8
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing


Dict
----


Dict[...]
---------


TypedDict
---------
* Since Python 3.8
* :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys


Optional Values
---------------


Default Values
--------------
* Does not support default values


NotRequired
-----------
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing


Required
--------
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing


Total
-----
* Since Python 3.11
* :pep:`655` –- Marking individual TypedDict items as required or potentially-missing


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing NamedTuple
=================


Tuple
-----


Tuple[str,str]
--------------


NamedTuple
----------


Default
-------


Extensibility
-------------


Contract
--------


Iteration
---------


IsInstance
----------


Equality
--------


Size
----


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing Callable
===============
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections


Return
------


Parameters
----------


Union
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Optional
--------


Alias
-----
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Exception
---------


Literal
-------
* Since Python 3.8: :pep:`586` -- Literal Types
* Literal de-duplicates parameters
* Equality comparisons of Literal objects are not order dependent
* https://docs.python.org/3/library/typing.html#typing.Literal


Callable
--------
* Function is Callable
* ``Callable``
* ``Callable[[int, int], float]`` is a function of ``(int, int) -> float``
* There is no syntax to indicate optional or keyword arguments
* https://docs.python.org/3/library/typing.html#typing.Callable


Iterator
--------
* All Generators are Iterators
* ``Generator[yield_type, send_type, return_type]``
* ``Iterator[yield_type]``


Annotations
-----------


Errors
------
* Python will execute without even warning
* Your IDE and ``mypy`` et. al. will yield errors


Good Engineering Practices
--------------------------


Literal String
--------------
* Since Python 3.11: :pep:`675` -- Arbitrary Literal String Type


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing Type
===========
* All classes are types
* Since 3.11: :pep:`673` - Self Type
* Since 3.7: ``from __future__ import annotations``
* https://peps.python.org/pep-0649/


Dynamic Attributes
------------------


Static Attributes
-----------------
* ClassVar indicates that a given attribute is intended to be used as a class variable and should not be set on instances of that class.
* https://docs.python.org/3/library/typing.html#typing.ClassVar


Method Return Type
------------------


Required Method Arguments
-------------------------


Optional Method Arguments
-------------------------


Init Method
-----------


Composition
-----------


Aggregation
-----------


Self
----


Instance
--------


Dependency Inversion Principle
------------------------------
* Always depend upon abstraction not an implementation
* More information in `OOP SOLID`


Final Class
-----------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing
* There is no runtime checking of these properties


Final Method
------------
* Since Python 3.8: :pep:`591` -- Adding a final qualifier to typing
* There is no runtime checking of these properties


Final Attribute
---------------
* A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass
* There is no runtime checking of these properties
* https://docs.python.org/3/library/typing.html#typing.Final


Future
------
* Since Python 3.12
* PEP-695 Type Parameter Syntax
* https://docs.python.org/3.12/whatsnew/3.12.html#whatsnew312-pep695


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`


Typing Annotated
================
* Since Python 3.9 :pep:`593` -- Flexible function and variable annotations
* https://docs.python.org/3/library/typing.html#typing.Annotated
* https://github.com/annotated-types/annotated-types
* https://github.com/tiangolo/fastapi/releases/tag/0.95.0


Numeric
-------


Character
---------


Patterns
--------


Typing Extra
============


TypeGuard
---------


TypeAlias
---------
* Since Python 3.10 :pep:`613` -- TypeAlias Annotation


TypeVar
-------


NewType
-------


Typing Deprecated
=================


Optional
--------
* Since Python 3.10 you can write ``int | None``
* ``Optional[int] == Union[int, None] == int | None``


Union
-----
* Since Python 3.10 you can write ``int | float``
* ``Union[int, str] == Union[str, int]``


List
----
* Since Python 3.9 you can write ``list[int]``


Tuple
-----
* Since Python 3.9 you can write ``tuple[int, ...]``


Set
---
* Since Python 3.9 you can write ``set[int]``


FrozenSet
---------
* Since Python 3.9 you can write ``frozenset[int]``


List[tuple]
-----------
* Since Python 3.9 you can write ``list[tuple]``


List[list]
----------
* Since Python 3.9 you can write ``list[list]``


Nested
------
* Since Python 3.9 you can write ``list[list|tuple|set]``


Dict
----
* Since Python 3.9 you can write ``dict[str,str]``


Typing Check
============


Python
------
* https://docs.python.org/3/howto/annotations.html
* ``inspect.get_annotations()``
* ``object.__annotations__``


MyPy
----
* Type Checking
* https://mypy-lang.org/
* https://github.com/python/mypy


PyType
------
* Pytype checks and infers types for your Python code - without requiring type annotations
* https://github.com/google/pytype
* https://pypi.org/project/pytype/


Pyre
----
* Pyre is a performant type checker for Python compliant with PEP 484. Pyre can analyze codebases with millions of lines of code incrementally – providing instantaneous feedback to developers as they write code
* https://pyre-check.org/
* https://pypi.org/project/pyre-check/


Typing Annotate
===============


PyAnnotate
----------
* Annotating existing code
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html


Monkeytype
----------
* Annotating existing code
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881


Typing Cython
=============
* https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html
* https://youtu.be/kFKRbo9tFNw?t=1244


Typing Mypyc
============
* Mypyc compiles Python modules to C extensions.
* It uses standard Python type hints to generate fast code.
* Source: https://mypyc.readthedocs.io/en/latest/


About
-----
* Source [#MypycDocs]_


Differences from Cython
-----------------------
* Source [#MypycDocs]_
* https://mypyc.readthedocs.io/en/latest/introduction.html#differences-from-cython
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python


How does it work
----------------
* Source [#MypycDocs]_


Development Status
------------------


Automation
----------


Configuration
-------------


Runtime type checking
---------------------
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python


Final values
------------
* Source [#MypycDocs]_


Recommended Workflow
--------------------
* Source [#MypycDocs]_


Further Reading
---------------
* https://mypyc.readthedocs.io/en/latest/
* https://mypyc.readthedocs.io/en/latest/introduction.html#differences-from-cython
* https://mypyc.readthedocs.io/en/latest/differences_from_python.html#differences-from-python
