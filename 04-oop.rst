

OOP Attribute Mutability
========================
* Function and method arguments should not be mutable


Problem
-------


Rationale
---------


Solution
--------


OOP Attribute ClassVar
======================
* Class Variables
* Instance Variables
* Type Annotations


Class Variables
---------------
* Fields defined on a class
* Must have default values
* Share state
* Also known as 'static attributes'


Instance Variables
------------------
* Fields defined on an instance
* Do not share state (unless mutable argument in method signature)
* By convention initialized in ``__init__()``
* Also known as 'dynamic attributes'


Class and Instance Variables
----------------------------


Annotations
-----------


Dataclass Fields
----------------
* Dataclass uses class variables notation to create instance fields
* Dataclass do not validate type annotations, unless ``ClassVar``


Init Variables
--------------


Class vs. Instance Variables
----------------------------


Mechanism
---------
* ``vars(obj)`` is will return ``obj.__dict__``


OOP Attribute Access Modifiers
==============================
* Attributes and methods are always public
* No protected and private keywords
* Private and protected is only by convention [#pydocprivatevar]_
* ``name`` - public attribute
* ``_name`` - protected attribute (non-public by convention)
* ``__name`` - private attribute (name mangling)
* ``__name__`` - system attribute (dunder)
* ``name_`` - avoid name collision with built-ins


Public Attribute
----------------
* ``name`` - public attribute


Protected Attribute
-------------------
* ``_attrname`` - protected attribute (non-public by convention)


Private Attribute
-----------------
* ``__attrname`` - private attribute (name mangling)


Name Mangling
-------------


Name Collision
--------------
* Example colliding names: ``type_``, ``id_``, ``hash_``


System Attributes
-----------------
* ``__attrname__`` - Current module
* ``obj.__class__`` - Class from which object was instantiated
* ``obj.__dict__`` - Stores instance variables
* ``obj.__doc__`` - Object docstring
* ``obj.__annotations__`` - Object attributes type annotations
* ``obj.__module__`` - Name of a module in which object was defined


Show Attributes
---------------
* ``vars()`` display ``obj.__dict__``


OOP Attribute Slots
===================
* Faster attribute access
* Space savings in memory (overhead of dict for every object)
* Prevents from adding new attributes
* The space savings is from:
* Store value references in slots instead of ``__dict__``
* Denying ``__dict__`` and ``__weakref__`` creation


Weakref
-------


Recap
-----


Declaration
-----------


Get Value
---------


Slots and Methods
-----------------


Slots and Init
--------------


Vars
----
* Using ``__slots__`` will prevent from creating ``__dict__``


Slots vs Attributes
-------------------


Slots Internals
---------------
* Slots are descriptors


Slots Dict
----------
* Docstring for slotted names
* Used for documentation


Get Attributes and Values
-------------------------
* To get values iterate over ``self.__slots__`` and use ``getattr(self, x)``


Slots and Dunder Dict
---------------------
* Using ``__slots__`` will prevent from creating ``__dict__``
* Adding ``__dict__`` to ``__slots__`` will combine both worlds


Inheritance
-----------
* Slots do not inherit, unless they are specified in subclass
* Slots are added on inheritance
* If class does not specify slots, the ``__dict__`` will be added


Change Slots
------------


Slots in Dataclasses
--------------------
* Since Python 3.10


Further Reading
---------------
* https://docs.python.org/3/reference/datamodel.html#slots
* https://stackoverflow.com/questions/472000/usage-of-slots


OOP Attribute Property
======================
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions such as ``ValueError`` or ``TypeError``
* Check argument type


Getter Only
-----------


Setter and Getter Methods
-------------------------
* Not only Java, but C++ and many others too


Pythonic Way
------------


Encapsulation
-------------


Protocol
--------
* ``myattribute = property()`` - creates property
* ``@myattribute.getter`` - getter for attribute
* ``@myattribute.setter`` - setter for attribute
* ``@myattribute.deleter`` - deleter for attribute
* Method name must be the same as attribute name
* ``myattribute`` has to be ``property``
* ``@property`` - creates property and a getter


Property class
--------------
* Property's arguments are method references ``get_name``, ``set_name``, ``del_name`` and a docstring
* Not recommended


Property Descriptor
-------------------
* Prefer ``name = property()``


Property Decorator
------------------
* Typically used when, there is only getter and no setter and deleter methods


OOP Method About
================
* ``name(self)`` - public method
* ``_name(self)`` - protected method (non-public by convention)
* ``__name(self)`` - private method (name mangling)
* ``__name__(self)`` - system method
* ``name_(self)`` - avoid name collision with built-ins


Recap
-----
* All functions are instances of a class ``function``
* All functions has attributes or methods such as ``__call__()``


Class Function
--------------


Method
------


Compare
-------


Types
-----


OOP Method Access Modifiers
===========================
* Attributes and methods are always public
* No protected and private keywords
* Protecting is only by convention [#pydocprivatevar]_
* ``name(self)`` - public method
* ``_name(self)`` - protected method (non-public by convention)
* ``__name(self)`` - private method (name mangling)
* ``__name__(self)`` - system method
* ``name_(self)`` - avoid name collision


Protected Method
----------------


Private Method
--------------


System Method
-------------


Show Methods
------------
* ``dir()``


OOP Method Staticmethod
=======================
* Should **not** be in a class: method which don't use ``self`` in its body
* Should be in class: if method takes ``self`` and use it (it requires instances to work)
* If a method don't use ``self`` but uses class as a namespace use ``@staticmethod`` decorator
* Using class as namespace
* No need to create a class instance
* Will not pass instance (``self``) as a first method argument


Problem
-------


Solution
--------


Dataclass
---------


Namespace
---------


OOP Method Classmethod
======================
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


Manifestation
-------------


OOP Inheritance Patterns
========================
* no inheritance
* single inheritance
* multilevel inheritance
* multiple inheritance (mixin classes)


No Inheritance
--------------


Single Inheritance
------------------


Multilevel Inheritance
----------------------


Multiple Inheritance
--------------------
* ``HasEngine`` and ``HasWindows`` are Mixin Classes
* Such classes are usually called: ``EngineMixin``, ``WindowsMixin``


Composition
-----------


Aggregation
-----------


Why Composition?
----------------


Further Reading
---------------
* https://github.com/django/django/blob/main/django/views/generic/base.py
* https://github.com/pandas-dev/pandas/blob/main/pandas/core/frame.py
* https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/linear_model/_base.py#L533


OOP Inheritance Problems
========================


About
-----


Problem
-------
* Code duplication


Simple Inheritance
------------------


Inheritance Problem
-------------------
* Motorcycle is a vehicle, but doesn't have windows


Not Implemented Error
---------------------


Multilevel Inheritance
----------------------


Problem
-------
* Code duplication or another multilevel inheritance
* For simplicity imagine if ``Truck`` cannot have passengers


Solution With Multilevel Inheritance
------------------------------------
* For simplicity imagine if ``Truck`` cannot have passengers
* ``Car`` is both ``VehicleWithWindows`` and ``VehicleWithPassengers``
* Causes more problem
* This is why in other languages composition is preferred over inheritance


Solution With Mixin Classes
---------------------------
* This is the Pythonic solution


OOP Inheritance Overload
========================
* Child inherits all fields and methods from parent
* Used to avoid code duplication


Overload Method
---------------


Overload Init
-------------


Overload ClassVars
------------------


Overload Attribute
------------------


OOP Inheritance Super
=====================


Super
-----
* Order is important
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_


Init and Multiple Inheritance
-----------------------------


Init Subclass
-------------


OOP Inheritance MRO
===================
* MRO - Method Resolution Order
* Inheritance Diamond


Problem
-------


Small Diamond
-------------


Large Diamond
-------------


Problematic super()
-------------------


Why?!
-----
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_


Compare
-------


Advanced
--------
* Source: [#Halterman2018]_
* Source: [#StackOverflowMRO]_


Ambiguous MRO
-------------


Further Reading
---------------
* van Rossum, G. Method Resolution Order. Year: 2010. Retrieved: 2022-07-13. URL: http://python-history.blogspot.com/2010/06/method-resolution-order.html


OOP Object Relations
====================
* ORM - Object-relational mapping
* Converts (`map`) between objects in code and database tables (`relations`)
* Declarative - First define model, which then maps to the database tables
* ``pickle`` - has relations
* ``json`` - has relations
* ``csv`` - non-relational format


Pros
----


Cons
----


OOP Object Identity
===================
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity


Identity
--------
* ``id(obj) -> int``
* ``id()`` will change every time you execute script
* ``id()`` returns an integer which is guaranteed to be unique and constant for object during its lifetime
* Two objects with non-overlapping lifetimes may have the same ``id()`` value
* In CPython it's also the memory address of the corresponding C object


Increment Add
-------------


Identity Check
--------------
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned
* Since Python 3.8 - Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.


Caching
-------


Integer Caching
---------------
* Values between -5 and 256 are cached from start
* After using any integer two times it is being cached
* Python caches also the next integer
* Cached numbers are invalidated after a while


Float Caching
-------------
* It takes a bit more hits for float to start being cached
* Cached numbers are invalidated after a while


Bool Type Identity
------------------
* Bool object is a singleton
* It always has the same identity (during one run)


None Type Identity
------------------
* NoneType object is a singleton
* It always has the same identity (during one run)


String Type Identity
--------------------


String Interning
----------------
* Caching mechanism
* String intern pool
* String is immutable


Type Identity
-------------


Object Identity
---------------


Object Equality
---------------


Value Comparison
----------------
* ``==`` checks for object equality


Compare Value vs. Identity
--------------------------


String Value vs Identity Problem
--------------------------------
* CPython optimization
* Can be misleading


Performance
-----------


OOP Object Constructor
======================


New Method
----------
* object constructor
* solely for creating the object
* ``cls`` as it's first parameter
* when calling ``__new__()`` you actually don't have an instance yet,


Init Method
-----------
* object initializer
* for initializing object with initial values
* ``self`` as it's first parameter
* ``__init__()`` is called after ``__new__()`` and the instance


Return
------


Injecting New
-------------


Do not Trigger Methods for User
-------------------------------
* It is better when user can choose a moment when call ``.connect()`` method


OOP Class Factory
=================


Class Definition
----------------


Static Attributes
-----------------


Static Methods
--------------


Dynamic Methods
---------------


Init Method
-----------


Class Inheritance
-----------------


Recap
-----


What is a class?
----------------


Dynamic Class Creation
----------------------


OOP Class Metaclass
===================
* Object is an instance of a class
* Class is an instance of a Metaclass


Recap
-----
* Functions are instances of a ``function`` class.


Syntax
------
* Metaclass is a callable which returns a class


Metaclasses
-----------
* Is a callable which returns a class
* Instances are created by calling the class
* Classes are created by calling the metaclass (when it executes the ``class`` statement)
* Combined with the normal ``__init__`` and ``__new__`` methods
* Class defines how an object behaves
* Metaclass defines how a class behaves


Metaclass as a function
-----------------------
* Function are classes


Usage
-----
* Metaclasses allow you to do 'extra things' when creating a class
* Allow customization of class instantiation
* Most commonly used as a class-factory
* Registering the new class with some registry
* Replace the class with something else entirely
* Inject logger instance
* Injecting static fields
* Ensure subclass implementation
* Metaclasses run when Python defines class (even if no instance is created)


Keyword Arguments
-----------------


Methods
-------
* ``__prepare__(metacls, name, bases, **kwargs) -> dict`` - on class namespace initialization
* ``__new__(metacls, classname, bases, attrs) -> cls`` - before class creation
* ``__init__(self, name, bases, attrs) -> None`` - after class creation
* ``__call__(self, *args, **kwargs)`` - allows custom behavior when the class is called


Type Metaclass
--------------


Method Resolution Order
-----------------------


Metaclass replacements
----------------------
* Effectively accomplish the same thing
