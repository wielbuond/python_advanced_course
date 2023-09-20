

Complexity
==========
* Computational Complexity
* Memory Complexity
* Cognitive Complexity
* Cyclomatic Complexity
* Big O notation [#wikibigonotation]_
* https://wiki.python.org/moin/TimeComplexity


Computational Complexity
------------------------


Memory Complexity
-----------------


Cognitive Complexity
--------------------
* Measure of how difficult the application is to understand
* Measure of how hard the control flow of a function is to understand
* Functions with high Cognitive Complexity will be difficult to maintain.
* https://www.sonarsource.com/docs/CognitiveComplexity.pdf


Cyclomatic Complexity
---------------------
* Measures the minimum number of test cases required for full test coverage.


Big O notation
--------------


Performance Optimization
========================
* https://wiki.python.org/moin/TimeComplexity


Contains
--------
* ``in`` checks whether iterable contains value
* O(n) - ``in str``
* O(n) - ``in list``
* O(n) - ``in tuple``
* O(1) - ``in set``
* O(1) - ``in dict``


PyPy
----
* http://pypy.org
* No GIL
* Can speedup couple order of magnitude


Patterns
--------
* Source: [#Shaw2022]_


Tools
-----
* memray [#Galindo2022]_
* tracemalloc
* mmap - memory allocation
* Pytest extension for doing benchmarking
* ``pip install line_profiler``


Numpy vectorization
-------------------


Specialized data structures
---------------------------
* ``scipy.spatial`` - for spatial queries like distances, nearest neighbours, etc.
* ``pandas`` - for SQL-like grouping and aggregation
* ``xarray`` - for grouping across multiple dimensions
* ``scipy.sparse`` - sparse metrics for 2-dimensional structured data
* ``sparse`` (package) - for N-dimensional structured data
* ``scipy.sparse.csgraph`` - for graph-like problems (e.g. finding shortest paths)


Cython
------
* https://numba.pydata.org/
* https://cython.readthedocs.io/en/latest/
* https://en.wikipedia.org/wiki/Cython
* https://youtu.be/zQeYx87mfyw?t=747
* types
* Cython files have a ``.pyx`` extension


Numba
-----


Dask
----
* https://dask.org


Find existing implementation
----------------------------
* https://pypi.org


String Concatenation
--------------------


String Append
-------------
* Use ``list.append()`` instead of ``str + str``:


Range between two ``float``
---------------------------
* There are indefinitely many values between two floats


Deque
-----
* ``collections.deque`` - Double ended Queue


Further Reading
---------------
* https://wiki.python.org/moin/TimeComplexity
* https://youtu.be/YY7yJHo0M5I
* https://visualgo.net/bn/sorting
* http://sorting.at/
* https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
* https://www.youtube.com/watch?v=fOdCxum-qLA
* https://www.youtube.com/watch?v=zQeYx87mfyw
* https://www.youtube.com/watch?v=EEUXKG97YRw


Micro-benchmarking
==================


Evaluation
----------
* Fresh start of Python process
* Clean memory before start
* Same data
* Same start conditions, CPU load, RAM usage, ``iostat``
* Do not measure how long Python wakes up
* Check what you measure


Timeit - Programmatic use
-------------------------
* ``timeit``


Timeit - Console use
--------------------


PyPerformance
-------------
* ``pip install pyperformance``
* ``pyperformance run -b django_template`` - run django template benchmark


Recap
-----


No Cache
--------


Global Scope
------------


Local Scope
-----------


Embedded Scope
--------------


Contains
--------


Get
---


Exceptions
----------


Layer
-----


Assignment Expression
---------------------


F-string
--------


string + string
---------------


str.format()
------------


%-style
-------


Prepare
-------


List Append If
--------------


List Append
-----------


Set Add
-------


Set Update
----------


Set Comprehension
-----------------


Set Comprehension Add
---------------------
* Add to Set Comprehension.
* Code appends generator object not values, this is why it is so fast!:


Set Comprehension Update
------------------------


Set Comprehension Update
------------------------


Set Comprehension Update Tuple
------------------------------


Set Comprehension Update List
-----------------------------


Set Comprehension Update Set
----------------------------


Comprehension Performance
=========================


Microbenchmark
--------------


Performance
-----------


Profiling
=========
* A profile is a set of statistics that describes how often and for how long various parts of the program executed
* The profiler modules are designed to provide an execution profile for a given program, not for benchmarking purposes (for that, there is timeit for reasonably accurate results). This particularly applies to benchmarking Python code against C code: the profilers introduce overhead for Python code, but not for C-level functions, and so the C code would seem faster than any Python one.


Profilers
---------
* cProfile (CPython built-in)
* yappi https://github.com/sumerc/yappi
* PyCharm IDE
* vmprof https://vmprof.readthedocs.io/en/latest/


Profiling with yappi
--------------------


Profiling with cProfile
-----------------------


Compilers and Interpreters
==========================
* https://docs.python.org/3/library/py_compile.html
* https://docs.python.org/3/library/compileall.html#module-compileall
* https://docs.python.org/3/library/zipapp.html


cPython
-------


Cython
------
* Cython is a compiled language that generates CPython extension modules
* Cython is a superset of the Python programming language
* Designed to give C-like performance with code that is written mostly in Python
* These extension modules can then be loaded and used by regular Python code using the import statement


PyPy
----


IronPython
----------


Jython
------


Micropython
-----------
* MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.
* MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.
* MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system.
* In addition to implementing a selection of core Python libraries, MicroPython includes modules such as "machine" for accessing low-level hardware.
* https://micropython.org/
* IoT


Pyston
------
* Pyston is an open-source faster implementation of the Python programming language, designed for the performance and compatibility challenges of large real-world applications.
* Pyston was started at Dropbox in 2014 in order to reduce the costs of its rapidly-growing Python server fleet.
* In 2019 the Pyston developers regrouped without a corporate sponsor and started investigating alternative approaches to speeding up Python. They ended up deciding to fork CPython 3.8, and by early 2020 they restarted the project in a new codebase, and called it "Pyston v2". The first version of Pyston v2 was released in late 2020.
* In mid-2021 the Pyston developers joined Anaconda, which since then has provided funding for the project and packaging expertise.
* https://www.pyston.org/
* https://github.com/pyston/pyston


GPython
-------
* gpython is a part re-implementation, part port of the Python 3.4 interpreter in Go.
* https://github.com/go-python/gpython


RustPython
----------
* RustPython is a Python interpreter written in Rust.
* RustPython can be embedded into Rust programs to use Python as a scripting language for your application, or it can be compiled to WebAssembly in order to run Python in the browser.
* RustPython is free and open-source under the MIT license.
* https://rustpython.github.io/


Cinder
------
* Cinder is Meta's (Facebook/Instagram) internal performance-oriented production version of CPython 3.8.
* It contains a number of performance optimizations, including bytecode inline caching, eager evaluation of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler that uses type annotations to emit type-specialized bytecode that performs better in the JIT.
* Cinder is powering Instagram, where it started, and is increasingly used across more and more Python applications in Meta.
* https://github.com/facebookincubator/cinder


PyScript
--------
* framework that allows users to create rich Python applications in the browser using a mix of Python with standard HTML. PyScript aims to give users a first-class programming language that has consistent styling rules, is more expressive, and is easier to learn.
* https://pyscript.net/
* https://github.com/pyscript/pyscript
* https://anaconda.cloud/pyscript-pycon2022-peter-wang-keynote


HPy
---
* HPy provides a new API for extending Python in C.
* In other words, you use #include <hpy.h> instead of #include <Python.h>.
* Zero overhead on CPython: extensions written in HPy runs at the same speed as "normal" extensions.
* Much faster on alternative implementations such as PyPy, GraalPython.
* Debug Mode: in debug mode, you can easily identify common problems such as memory leaks, invalid lifetime of objects, invalid usage of APIs. Have you ever forgot a Py_INCREF or Py_DECREF? The HPy debug mode will detect these mistakes for you.
* Universal binaries: extensions built for the HPy Universal ABI can be loaded unmodified on CPython, PyPy, GraalPython, etc.
* Nicer API: the standard Python/C API shows its age. HPy is designed to overcome some of its limitations, be more consistent, produce better quality extensions and to make it harder to introduce bugs.
* Evolvability: As nicely summarized in [PEP-620](https://peps.python.org/pep-0620/) the standard Python/C API exposes a lot of internal implementation details which makes it hard to evolve the C API. HPy doesn't have this problem because all internal implementation details are hidden.
* https://hpyproject.org/


GraalPython
-----------
* High-Performance. Modern Python
* On average, Python in GraalVM is 8.92x faster than CPython and 8.34x faster than Jython
* GraalVM provides a Python 3.8 compliant runtime.
* A primary goal of the GraalVM Python runtime is to support SciPy and its constituent libraries, as well as to work with other data science and machine learning libraries from the rich Python ecosystem.
* https://www.graalvm.org/python/


Cython
------
* https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html


Mypyc
-----
* Mypyc compiles Python modules to C extensions.
* It uses standard Python type hints to generate fast code.
* https://mypyc.readthedocs.io/en/latest/


Nuitka
------
* https://www.nuitka.net


Others
------


Compiling
---------
* https://py2app.readthedocs.io/
* http://www.py2exe.org/
* http://www.pyinstaller.org/
