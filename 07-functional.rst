

Functional About
================
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens
* Functional programming avoids side effects
* Functional programming provides referential transparency
* Instead of loop use ``map`` and recurrence
* Functions can be bound to names (including local identifiers), passed as arguments, and returned from other functions, just as any other data type can [#WikipediaFunc]_
* Imperative program will use a loop to traverse and modify a list, while a functional program, would prefer using a higher-order ``map`` function that takes a function and a list, generating and returning a new list by applying the function to each list item [#Spiewak2008]_
* Restricting side effects, can decrease number of bugs, be easier to debug and test, and be more suited to formal verification [#Hughes1984]_ [#Hudak1989]_
* Functional Design Patterns - Scott Wlaschin https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY


Advantages
----------
* Comprehensibility: Pure functions don't change states and are entirely dependent on input, and are consequently simple to understand.
* Concurrency: As pure functions avoid changing variables or any data outside it, concurrency implementation is easier.
* Lazy evaluation: Functional programming encourages lazy evaluation, which means that the value is evaluated and stored only when required.
* Easier debugging and testing: Pure functions take arguments once and produce unchangeable output. With immutability and no hidden output, debugging and testing becomes easier.


Disadvantages
-------------
* Potentially poorer performance: Immutable values combined with recursion might lead to a reduction in performance.
* Coding difficulties: Though writing pure functions is easy, combining it with the rest of the application and I/O operations can be tough.
* No loops can be challenging: Writing programs in a recursive style instead of loops can be a daunting task.


Applications
------------


Further Reading
---------------
* Functional Design Patterns - Scott Wlaschin - https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY


Doctests
--------


Functional Map
==============
* Map (convert) elements in sequence
* Generator (lazy evaluated)
* ``map(callable, *iterables)``
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Multi Parameters
----------------


Starmap
-------


Partial
-------


Performance
-----------


Functional Filter
=================
* ``filter(callable, *iterables)``
* Select elements from sequence
* Generator (lazy evaluated)
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects


Problem
-------


Solution
--------


Lazy Evaluation
---------------


Performance
-----------


Functional Reduce
=================
* Reduce sequence using function
* Built-in


Syntax
------
* ``functools.reduce(function, iterable[, initializer])``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object
* https://docs.python.org/library/functools.html


Problem
-------


Solution
--------


Rationale
---------
* https://docs.python.org/library/operator.html


Map Reduce
----------
* https://dask.org


Functional Lambda
=================
* Lambda - Anonymous functions
* When function is used once
* When function is short
* You don't need to name it (therefore anonymous)


Syntax
------


Convention
----------
* Usually parameters are named ``x`` and ``y``
* Use shortest code possible
* Do not assign ``lambda`` to variable
* Lambda is anonymous function and it should stay anonymous. Do not name it
* :pep:`8` -- Style Guide for Python Code: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier". Lambda is anonymous function and it should stay anonymous. Do not name it.
* Usually there are no spaces in lambda expressions (to make code shorter)


Note to Programmers of Different Languages
------------------------------------------


Noop
----


Lambda with Map
---------------


Lambda with Filter
------------------


Performance
-----------


Further Reading
---------------
* https://youtu.be/eis11j_iGMs


Functional Scope
================
* Values defined in function does not leak out
* Functions has access to global values
* Shadowing is when you define variable with name identical to the one


Values Leaking
--------------
* Values defined in function does not leak out


Outer Scope
-----------
* Functions has access to global values


Shadowing
---------
* When variable in function has the same name as in outer scope
* Shadowing in a function is valid only in a function
* Shadowed variable will be deleted upon function return
* After function return, the original value of a shadowed variable


Global
------
* ``global`` keyword allows modification of global variable
* Using ``global`` keyword is considered as a bad practice


Nonlocal
--------
* Python nonlocal keyword is used to reference a variable in the nearest scope


Global Scope
------------


Local Scope
-----------
* Variables defined inside function
* Variables are not available from outside
* If outside the function, will return the same as ``globals()``


Shadowing Global Scope
----------------------
* Defining variable with the same name as in outer scope
* Shadowed variable will be deleted upon function return


Builtins
--------


Functional Pure Functions
=========================
* Pure functions have no side effects (i.e. memory, state, I/O)
* Calling the pure function again with the same arguments returns the same result (this can enable caching optimizations such as memoization)
* If the result of a pure expression is not used, it can be removed without affecting other expressions
* If there is no data dependency between two pure expressions, their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (the evaluation of any pure expression is thread-safe) [#WikipediaFunc]_


Pure Function
-------------


Impure Function
---------------


Impure to Pure Function
-----------------------


Side Effects
------------
* I/O - Input Output
* Looks like a pure function
* File content can change by other process


Functional Recurrence
=====================
* Also known as recursion
* Iteration in functional languages is usually accomplished via recursion
* Recursive functions invoke themselves
* Operation is repeated until it reaches the base case
* In general, recursion requires maintaining a stack, which consumes space


Recurrence in Python
--------------------
* Python isn't a functional language
* CPython implementation doesn't optimize tail recursion
* Tail recursion is not a particularly efficient technique in Python
* Rewriting the algorithm iteratively, is generally a better idea
* Uncontrolled recursion causes stack overflows!


Recursion Depth Limit
---------------------
* Default recursion depth limit is 1000
* Warning: Anaconda sets default recursion depth limit to 2000


Functional Immutable
====================
* Purely functional data structures have persistence
* (keeps previous versions of the data structure unmodified)


Mutable vs Immutable
--------------------


Changes
-------


Immutable Types
---------------
* ``int``
* ``float``
* ``complex``
* ``bool``
* ``None``
* ``str``
* ``bytes``
* ``tuple``
* ``frozenset``
* ``mappingproxy``


Mutable Types
-------------
* ``list``
* ``set``
* ``dict``


Comparison
----------


Array
-----


Mutable Dataclass
-----------------


Immutable Dataclass
-------------------


Functional First-Class
======================
* Function can be assigned to variable
* Function can be stored in data structures such as hash tables, lists, ...
* Function can be returned
* Function can be user as a parameter


Assigning Functions
-------------------
* Function can be assigned to variable


Storing Functions
-----------------
* Function can be stored in data structures such as hash tables, lists, ...


Returning Functions
-------------------
* Function can be returned


Parameter Functions
-------------------
* Function can be user as a parameter


Functional Higher-Order
=======================
* Function can take other function as arguments
* Function can return function


Calling
-------


Functional Referential Transparency
===================================
* Value of a variable in a functional program never changes once defined
* This eliminates any chances of side effects
* Any variable can be replaced with its actual value at any point of execution [#Hughes1984]_


Functional Namespace
====================
* Functions provide namespaces
* Only code inside that namespace can access it's locals


Variables Inside Function
-------------------------
* Variables inside function


Functions Inside Function
-------------------------
* Functions inside function


Classes Inside Function
-----------------------


Methods Inside Function
-----------------------


Instances Inside Function
-------------------------


All Together
------------


Execute
-------


Return Results
--------------


Return Function
---------------


Locals
------


Functional Function Attributes
==============================


Name
----
* ``function.__name__``
* ``function.__qualname__``


Type
----
* ``type(function)``
* ``function.__class__``
* ``function.__class__.__name__``
* ``function.__class__.__qualname__``
* ``function.__class__.__text_signature__``


Annotations
-----------


Signature
---------


Doc
---
* ``help(function)``
* ``function.__doc__``


Call
----
* ``callable(function)``
* ``function()``
* ``function.__call__()``


Setattr, Getattr
----------------


Function Code
-------------


Functional Callable
===================


Calling Call Method
-------------------
* ``__call__()`` method makes object callable


Overloading Call Method
-----------------------


Typing
------


Functional Pattern Closure
==========================
* Technique by which the data is attached to some code even after end of those other original functions is called as closures
* When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants
* Inner functions implicitly carry references to all of the local variables in the surrounding scope that are referenced by the function
* Since Python 2.2


Recap
-----


Nested Function
---------------
* Function inside the function
* Nested functions can access the variables of the enclosing scope


What is closure?
----------------


Why?
----
* Closures provides some form of data hiding
* Closures can avoid use of global variables
* Useful for replacing hard-coded constants


How Objects Were Born
---------------------
* ``main`` - constructor
* ``say_hello`` - instance method
* ``firstname`` - instance variable (field)
* ``lastname`` - instance variable (field)


Functional Pattern Callback
===========================
* Callback Design Pattern


Functional Pattern MapReduce
============================
* split-apply-combine strategy


Pattern
-------


Usage
-----


Functional Pattern Maybe
========================
* Maybe monad
* Continues execution, even, if there is an error
* Final state will be none
* But no intermediate error handling is needed


Pattern
-------


With Value
----------


With Errors
-----------


Functional Stdlib Functools
===========================
* ``import functools``
* ``functools.partial()``
* ``functools.partialmethod()``
* ``functools.reduce()``
* ``functools.singledispatch()``
* ``functools.singledispatchmethod()``


Partial
-------
* Create alias function and its arguments
* Useful when you need to pass function with arguments to for example ``map`` or ``filter``


Partialmethod
-------------


Reduce
------
* split-apply-combine strategy


Singledispatch
--------------
* Since Python 3.4
* Overload a method
* Python will choose function to run based on argument type


Singledispatchmethod
--------------------
* Since Python 3.8
* Overload a method
* Python will choose method to run based on argument type


Operator Module
===============
* ``operator.add()``
* ``operator.sub()``
* ``operator.mul()``
* ``operator.truediv()``
* ``operator.floordiv()``
* ``operator.mod()``
* ``operator.pow()``
* ``operator.matmul()``
* ``operator.neg()``
* ``operator.pos()``
* ``operator.invert()``


Operator Module - AND
---------------------


Operator Module - OR
--------------------


Operator Module - XOR
---------------------


Reduce
------


Methodcaller
------------


Reduce
------


Map-Reduce
----------
