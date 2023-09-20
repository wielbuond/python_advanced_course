

Decorator About
===============
* Decorator is an object, which takes another object as it's argument
* Since Python 2.4: :pep:`318` -- Decorators for Functions and Methods
* Since Python 3.9: :pep:`614` -- Relaxing Grammar Restrictions On Decorators
* Decorator can do things before call
* Decorator can do things after call
* Decorator can modify arguments
* Decorator can modify returned value
* Decorator can avoid calling
* Decorator can modify globals
* Decorator can add or change metadata


Syntax
------
* ``func`` is a reference to function which is being decorated
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments


Decoration
----------


Decorator Types
===============
* Decorator function
* Decorator method
* Decorator class


Decorator Function
------------------
* Decorator is a function which takes another object as an argument
* Doesn't matter, whether this object is a function, class or method


Decorator Method
----------------
* Decorator is a method which takes instance and another object as an argument
* Doesn't matter, whether this object is a function, class or method


Decorator Class
---------------
* Decorator is a class which takes another object as an argument to ``__init__()`` method
* Doesn't matter, whether this object is a function, class or method


Decorator Wrapper
=================
* Wrapper function
* Wrapper lambda
* Wrapper class
* Wrapper method


Name
----
* Name ``wrapper`` is just a convention


Wrapper Function
----------------
* ``obj`` is a decorated object
* Doesn't matter, whether is a function, class or method


Wrapper Lambda
--------------
* ``obj`` is a decorated object
* Doesn't matter, whether is a function, class or method


Wrapper Class
-------------
* If ``obj`` and ``Wrapper`` are classes, ``Wrapper`` can inherit from ``obj`` (to extend it)


Wrapper Arguments
-----------------
* If you know names of the arguments you can use it in wrapper
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments


Decorator About Object
======================
* Decorating function
* Decorating class
* Decorating method


Decorating Function
-------------------
* By convention ``func`` or ``fn``


Decorating Class
----------------
* By convention ``cls``


Decorating Method
-----------------
* By convention ``mth``, ``meth`` or ``method``


Decorator About Arguments
=========================
* Without Arguments
* With Positional Arguments
* With Mixed Arguments
* With Keyword Arguments


Without Arguments
-----------------


With Positional Arguments
-------------------------


With Mixed Arguments
--------------------


With Keyword Arguments
----------------------


Decorate Function
=================
* Decorator must return reference to ``wrapper``
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``function``


Decorate Stacked
================


Decorate Method
===============
* ``mydecorator`` is a decorator name
* ``method`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments


Syntax
------
* ``mydecorator`` is a decorator name
* ``mymethod`` is a method name
* ``self`` is an instance
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments


Decorate Class
==============
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name


Syntax
------
* ``mydecorator`` is a decorator name
* ``MyClass`` is a class name


Decorator Function
==================
* ``func`` is a reference to function which is being decorated
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments
* By calling ``func(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments


Decorator Method
================
* ``MyClass`` is a class containing decorator
* ``mydecorator`` is a decorator name
* ``myfunction`` is a function name
* ``func`` is a reference to function which is being decorated


Decorator Class
===============
* ``MyDecorator`` is a decorator name
* ``myfunction`` is a function name
* ``func`` is a reference to function which is being decorated


Decorator Arguments
===================
* Used for passing extra configuration to decorators
* Use more one level of nesting


Decorator Stdlib Functools
==========================


Wraps
-----
* ``from functools import wraps``
* ``@wraps(func)``


Cached Property
---------------
* ``from functools import cached_property``
* ``@cached_property(method)``


LRU (least recently used) cache
-------------------------------
* ``from functools import lru_cache``
* ``@lru_cache(maxsize=None)``


Decorator Recap
===============


Function Decorators with Function Wrappers
------------------------------------------


Function Decorators with Class Wrappers
---------------------------------------


Class Decorators
----------------
