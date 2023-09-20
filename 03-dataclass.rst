

Dataclass About
===============
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes
* This are not static fields!
* Dataclasses require Type Annotations


Problem
-------


Solution
--------


Dataclass Define Basic
======================


Required Fields
---------------


Default Fields
--------------


Lists
-----


Dataclass Define Special
========================


Union Fields
------------


Optional Fields
---------------


Literal Field
-------------


ClassVar Fields
---------------
* ``from typing import ClassVar``
* Defines static field


Keyword Arguments Only
----------------------
* Since Python 3.10
* ``from dataclasses import KW_ONLY``


Dataclass Define Nested
=======================


Relation to Objects
-------------------


Relation to Self
----------------
* Note, that there are ``None`` default friends
* Using an empty list ``[]`` as a default value will not work
* ``Self`` is available since Python 3.11
* We will cover this topic later


Dataclass Mechanism
===================


Input
-----


Output
------


Dataclass Postinit
==================
* Dataclasses generate ``__init__()``
* Overloading ``__init__()`` manually will destroy it
* For init time validation there is ``__post_init__()``
* It is run after all parameters are set in the class
* Hence you have to take care about negative cases (errors)


Initial Validation in Classes
-----------------------------
* Init serves not only for fields initialization
* It could be also used for value validation


Initial Validation in Dataclasses
---------------------------------
* Creating own ``__init__()`` will overload init from dataclasses
* Therefore in dataclasses there is ``__post_init__()`` method
* It is run after init (as the name suggest)
* It works on fields, which already saved (it was done in ``__init__``)
* No need to assign it once again
* You can focus only on bailing-out (checking only negative path - errors)


Date and Time Conversion
------------------------
* ``__post_init__()`` can also be used to convert data
* Example str ``1969-07-21`` to date object ``date(1969, 7, 21)``


InitVar
-------
* Init-only fields
* Added as parameters to the generated ``__init__``
* Passed to the optional ``__post_init__`` method
* They are not otherwise used by Data Classes


Dataclass Mutable Attrs
=======================
* problem with ``dict``, ``list``, ``set``
* You should not set mutable objects as a default function argument
* ``field()`` creates new empty ``list`` for each object
* It does not reuse reference
* Discussion: https://github.com/ericvsmith/dataclasses/issues/3


Problem
-------


List of Strings
---------------


List of Objects
---------------


Dict
----


Default Values
--------------


Dataclass Field
===============
* ``default`` - Default value for the field
* ``default_factory`` - Field factory
* ``init`` - Use this field in ``__init__()``
* ``repr`` - Use this field in ``__repr__()``
* ``hash`` - Use this field in ``__hash__()``
* ``compare`` - Use this field in comparison functions (le, lt, gt, ge, eq, ne)
* ``metadata`` - For storing extra information about field
* ``kw_only`` - field will become a keyword-only parameter to ``__init__()``


Default
-------
* ``default`` - Default value for the field


Default Factory
---------------
* ``default_factory`` - Field factory


Init
----


Repr
----


kw_only
-------
* Since Python 3.10
* keyword-only


Dataclass Metadata
==================
* ``metadata`` - For storing extra information about field
* ``dict | None``
* ``None`` is treated as an empty ``dict``
* Metadata is not used at all by Data Classes
* Metadata is provided as a third-party extension mechanism
* Use Case: SQLAlchemy https://python3.info/database/sqlalchemy/model-dataclass.html


Syntax
------


Validation
----------


Dataclass Parameters
====================
* ``init`` - Generate ``__init__()`` method
* ``repr`` - Generate ``__repr__()`` method
* ``eq`` - Generate ``__eq__()`` and ``__ne__()`` methods
* ``order`` - Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods
* ``unsafe_hash`` - If False: the ``__hash__()`` method is generated according to how eq and frozen are set
* ``frozen`` - If ``True``: assigning to fields will generate an exception
* ``match_args`` - Generate ``__match_args__()`` method
* ``kw_only`` - Mark all fields as keyword-only
* ``slots`` - Create class with ``__slots__``


Init
----
* ``init=True`` by default
* Generate ``__init__()`` method


Repr
----
* ``repr=True`` by default
* Generate ``__repr__()`` for pretty printing


Frozen
------
* ``frozen=False`` by default
* Prevents object from modifications
* Assigning to fields will generate an exception


Hash
----
* ``hash=False`` by default
* the ``__hash__()`` method is generated according to how eq and frozen are set


Order
-----
* ``order=False`` by default
* Generate ``__lt__()``, ``__le__()``, ``__gt__()``, and ``__ge__()`` methods


Match_args
----------
* ``match_args=True`` by default
* Since Python 3.10


Kw_only
----------
* ``kw_only=False`` by default
* Mark all fields as keyword-only
* Since Python 3.10


Slots
-----
* ``slots=False`` by default
* Create class with ``__slots__``
* Since Python 3.10


Dataclass Helpers
=================
* ``fields()`` - Returns a tuple of Field objects
* ``asdict()`` - converts the dataclass to a dict
* ``astuple()`` - converts the dataclass to a tuple
* ``make_dataclass()`` - creates a new dataclass
* ``replace()`` - replaces field of a dataclass
* ``is_dataclass()`` - checks if argument is a dataclass


Fields
------
* ``fields(class_or_instance)``


As Dict
-------
* ``asdict(instance, *, dict_factory=dict)``


As Tuple
--------
* ``astuple(*, tuple_factory=tuple)``


Make Dataclass
--------------
* ``make_dataclass(cls_name, fields, *, bases=(), namespace=None)``


Replace
-------
* ``replace(instance, **changes)``


Is Dataclass
------------
* ``is_dataclass(class_or_instance)``


Dataclass Inheritance
=====================
* Dataclasses can inherit from other classes
* Superclass not necessarily has to be dataclass
* If parent is dataclass the init will be joined


Inheritance
-----------


Post Init
---------


Super
-----


Dataclass Introspect
====================


Introspect Function
-------------------
* Source: https://stackoverflow.com/a/67232265


Simple
------


Complex
-------
