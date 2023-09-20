

Protocol Interface
==================
* Python don't have interfaces, although you can achieve similar effect
* Since Python 3.8 there are Protocols, which effectively are interfaces
* Interfaces cannot be instantiated
* Interfaces can be implemented
* Implemented class must define all interface methods (implement interface)
* Only public method declaration


Problem
-------


Solution
--------
* S.O.L.I.D.
* DIP - Dependency Inversion Principle
* Always depend on an abstraction not con


Interface Names
---------------
* ``Cache``
* ``CacheInterface``
* ``CacheIface``
* ``ICache``


Alternative Notation
--------------------


Not Existing Notation
---------------------
* This currently does not exists in Python
* In fact it is not even a valid Python syntax
* But it could greatly improve readability


Protocol Abstract Class
=======================
* Since Python 3.0: :pep:`3119` -- Introducing Abstract Base Classes
* Cannot instantiate
* Possible to indicate which method must be implemented by child
* Inheriting class must implement all methods
* Some methods can have implementation
* Python Abstract Base Classes [#pydocabc]_


Syntax
------
* Inherit from ``ABC``
* At least one method must be ``abstractmethod`` or ``abstractproperty``
* Body of the method is not important, it could be ``raise NotImplementedError`` or ``pass``


Implement Abstract Methods
--------------------------
* All abstract methods must be covered
* Abstract base class can have regular (not abstract) methods
* Regular methods will be inherited as normal
* Regular methods does not need to be overwritten


ABCMeta
-------
* Uses ``metaclass=ABCMeta``
* Not recommended since Python 3.4
* Use inheriting ``ABC`` instead


Abstract Property
-----------------
* ``abc.abstractproperty`` is deprecated since Python 3.3
* Use ``property`` with ``abc.abstractmethod`` instead


Problem: Base Class Has No Abstract Method
------------------------------------------


Problem: Base Class Does Not Inherit From ABC
---------------------------------------------


Problem: All Abstract Methods are not Implemented
-------------------------------------------------


Problem: Some Abstract Methods are not Implemented
--------------------------------------------------


Problem: Child Class has no Abstract Property
---------------------------------------------
* Using ``abstractproperty``


Problem: Child Class has no Abstract Properties
-----------------------------------------------
* Using ``property`` and ``abstractmethod``


Problem: Invalid Order of Decorators
------------------------------------
* Invalid order of decorators: ``@property`` and ``@abstractmethod``
* Should be: first ``@property`` then ``@abstractmethod``


Problem: Overwrite ABC File
---------------------------


Further Reading
---------------
* https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes
* https://www.youtube.com/watch?v=S_ipdVNSFlo


Protocol Structural
===================
* :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.8
* Protocol describe an interface, not an implementation
* Protocol classes should not have method implementations
* Protocol can describe both methods and attributes


Standard Library Protocols
--------------------------
* ``from collections.abc import *``
* ``Container``
* ``Hashable``
* ``Iterable``
* ``Iterator``
* ``Reversible``
* ``Generator``
* ``Callable``
* ``Collection``
* ``Sequence``
* ``MutableSequence``
* ``ByteString``
* ``Set``
* ``MutableSet``
* ``Mapping``
* ``MutableMapping``
* ``MappingView``
* ``ItemsView``
* ``KeysView``
* ``ValuesView``
* ``Awaitable``
* ``Coroutine``
* ``AsyncIterator``
* ``AsyncGenerator``


Terminology
-----------


Explicit Subtyping
------------------
* ``Email`` is explicit subclass of the protocol


Structural Subtyping
--------------------
* If an object that has all the protocol attributes it implements it
* Structural subtyping is natural for Python programmers
* Matches the runtime semantics of duck typing
* ``Email`` is structural subtype of a protocol (it conforms to structure)
* ``Email`` is implicit subtype of the protocol ``Message`` (not inherits)
* ``Email`` implement the protocol ``Message``
* ``Email`` is compatible with a protocol ``Message``


What Protocols are Not?
-----------------------
* At runtime, protocol classes is simple ABC
* No runtime type check
* Protocols are completely optional


Covariance, Contravariance, Invariance
--------------------------------------
* https://www.youtube.com/watch?v=1IiL31tUEVk&t=445s
* Covariance - Enables you to use a more derived type than originally specified
* Contravariance - Enables you to use a more generic (less derived) type than originally specified
* Invariance - Means that you can use only the type originally specified.
* Invariance is important for example in ``np.ndarray``, where all items must be exactly the same type


Default Value
-------------


Merging and extending protocols
-------------------------------


Generic Protocols
-----------------


Recursive Protocols
-------------------
* Since 3.11 :pep:`673` –- Self Type
* Since 3.7 ``from __future__ import annotations``
* Future :pep:`563` -- Postponed Evaluation of Annotations


Unions
------


Modules as implementations of protocols
---------------------------------------


Callbacks
---------


Runtime Checkable
-----------------
* By default ``isinstance()`` and ``issubclass()`` won't work with protocols
* You can use ``typing.runtime_checkable`` decorator to make it work


Protocol Polymorphism
=====================


Elif
----


Match: Switch Pattern
---------------------
* Since Python 3.10: :pep:`636` -- Structural Pattern Matching: Tutorial
* More information :ref:`Match About` [#pybookSyntaxMatch]_


Procedural Polymorphism
-----------------------
* UNIX ``getchar()`` function used function lookup table with pointers


Explicit Polymorphism
---------------------


Structural Polymorphism
-----------------------
* Duck typing


Protocol About
==============
* :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.8
* Protocol describe an interface, not an implementation
* Protocol classes should not have method implementations
* Protocol can describe both methods and attributes


Standard Library Protocols
--------------------------
* ``from collections.abc import *``
* ``Container``
* ``Hashable``
* ``Iterable``
* ``Iterator``
* ``Reversible``
* ``Generator``
* ``Callable``
* ``Collection``
* ``Sequence``
* ``MutableSequence``
* ``ByteString``
* ``Set``
* ``MutableSet``
* ``Mapping``
* ``MutableMapping``
* ``MappingView``
* ``ItemsView``
* ``KeysView``
* ``ValuesView``
* ``Awaitable``
* ``Coroutine``
* ``AsyncIterator``
* ``AsyncGenerator``


Terminology
-----------


Explicit Subtyping
------------------
* ``Email`` is explicit subclass of the protocol


Structural Subtyping
--------------------
* If an object that has all the protocol attributes it implements it
* Structural subtyping is natural for Python programmers
* Matches the runtime semantics of duck typing
* ``Email`` is structural subtype of a protocol (it conforms to structure)
* ``Email`` is implicit subtype of the protocol ``Message`` (not inherits)
* ``Email`` implement the protocol ``Message``
* ``Email`` is compatible with a protocol ``Message``


What Protocols are Not?
-----------------------
* At runtime, protocol classes is simple ABC
* No runtime type check
* Protocols are completely optional


Covariance, Contravariance, Invariance
--------------------------------------
* https://www.youtube.com/watch?v=1IiL31tUEVk&t=445s
* Covariance - Enables you to use a more derived type than originally specified
* Contravariance - Enables you to use a more generic (less derived) type than originally specified
* Invariance - Means that you can use only the type originally specified.
* Invariance is important for example in ``np.ndarray``, where all items must be exactly the same type


Default Value
-------------


Merging and extending protocols
-------------------------------


Generic Protocols
-----------------


Recursive Protocols
-------------------
* Since 3.11 :pep:`673` –- Self Type
* Since 3.7 ``from __future__ import annotations``
* Future :pep:`563` -- Postponed Evaluation of Annotations


Unions
------


Modules as implementations of protocols
---------------------------------------


Callbacks
---------


Runtime Checkable
-----------------
* By default ``isinstance()`` and ``issubclass()`` won't work with protocols
* You can use ``typing.runtime_checkable`` decorator to make it work


Protocol Iterator
=================
* Used for iterating in a ``for`` loop
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``
* ``iter(obj)`` -> ``obj.__iter__()``
* ``next(obj)`` -> ``obj.__next__()``


Loop and Iterators
------------------


Protocol Context Manager
========================
* ``__enter__(self) -> self``
* ``__exit__(self, *args) -> None``
* ``__leave__()`` https://github.com/faster-cpython/ideas/issues/550#issuecomment-1410120100
* Since Python 3.10: Parenthesized context managers [#pydocpython310]_
* https://peps.python.org/pep-0707/
* Files
* Buffering data
* Database connection
* Database transactions
* Database cursors
* Locks
* Network sockets
* Network streams
* HTTP sessions


Typing
------
* ``contextlib.AbstractContextManager``
* ``contextlib.AbstractAsyncContextManager``


Contex Manager
--------------


Context Decorator Class
-----------------------
* Inherit from ``contextlib.ContextDecorator``
* Class become context manager decorator
* Mind the brackets in decorator ``@Timeit()``


Context Decorator Function
--------------------------
* Split function for parts before and after ``yield``
* Code before ``yield`` becomes ``__enter__()``
* Code after ``yield`` becomes ``__exit__()``


Many Context Managers
---------------------
* https://docs.python.org/3/whatsnew/3.10.html#parenthesized-context-managers


Protocol Descriptor
===================
* Add managed attributes to objects
* Outsource functionality into specialized classes
* Descriptors: ``classmethod``, ``staticmethod``, ``property``, functions in general
* ``__del__(self)`` is reserved when object is being deleted by garbage collector (destructor)
* ``__set_name()`` After class creation, Python default metaclass will call it with cls and classname


Protocol
--------
* ``__get__(self, cls, *args) -> self``
* ``__set__(self, cls, value) -> None``
* ``__delete__(self, cls) -> None``
* ``__set_name__(self)``


Property vs Reflection vs Descriptor
------------------------------------


Inheritance
-----------


Function Descriptor
-------------------
* Function are Descriptors too
