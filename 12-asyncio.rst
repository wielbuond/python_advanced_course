

About
=====
* Latency problem - time from the user action to the appearance of the first UI element user can interact with
* General rule for frontend frameworks - don't block the foreground, let the long running operations to run in background, and leave the user interface interactive
* Concurrency and Parallelism


Classification of concurrency problems
--------------------------------------
* Martelli Model of Scalability
* 1 core: Single thread and single process
* 2-8 cores: Multiple threads and multiple processes
* 9+ cores: Distributed processing


GIL
---
* Global Interpreter Lock
* CPython has a lock for its internal shared global state
* One lock instead of hundreds smaller
* The unfortunate effect of GIL is that no more than one thread can run at a time
* For I/O bound applications, GIL doesn't present much of an issue
* For CPU bound applications, using threads makes the application speed worse
* Accordingly, that drives us to multiprocessing to gain more CPU cycles
* Larry Hastings, Gilectomy project - removed GIL, but Python slowed down


Process
-------


Thread
------


Async
-----
* Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
* Async is the future of programming


Sync vs Async
-------------


Threads vs Processes
--------------------


Threads vs Async
----------------
* Threads are about workers and async is about tasks
* Async maximizes CPU utilization because it has less overhead than threads.
* Threading typically works with existing code and tools as long as locks are added around critical sections
* For complex systems, async is much easier to get right than threads with locks
* Threads require very little tooling (locks and queues)
* Async needs a great deal of tooling (futures, event loops, and non-blocking version of just about everything.


Context Switching
-----------------
* Threads, thread manager does it automatically for you
* In Async, you specify places to context switch
* Time consuming
* Za każdym razem kiedy robisz ``print()`` kod automatycznie wykonuje Context Switch


Testing
-------
* In concurrent programs (threading, multiprocessing) testing can hide bugs and errors
* Some lines of code works so fast, that it requires million runs to make errors to appear
* But if you put ``sleep()`` than errors will show up
* In Internet of Things (IoT) I'd prefer to stand in front of a car which has code written in async way, than a threaded way
* Async is profoundly easier to debug and get it right


Rules
-----


AsyncIO About
=============
* ``asyncio`` in Python standard library
* ``async`` and ``await`` builtin keywords
* Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
* Async is the future of programming


Advantages
----------
* Maximize the usage of a single thread
* Handling I/O asynchronously
* Enabling concurrent code using coroutines
* Async will fill the gaps, otherwise wasted on waiting for I/O
* You control when tasks switches occur, so locks and other synchronization are no longer needed
* Async is the cheapest way to task switch
* Cost task switches is incredibly low; calling a pure Python function has more overhead than restarting a generator or awaitable
* Function builds stack each time it's called, whereas async uses generators underneath, which already has stack created
* In terms of speed async servers blows threaded servers in means of thousands
* Async is very cheap in means of resources
* Async world has a huge ecosystem of support tools
* Coding is easier to get right, than threads


Disadvantages
-------------
* Async switches cooperatively, so you do need to add explicit code ``yield`` or ``await`` to cause a task to switch
* Everything you do need a non-blocking version (for example ``open()``)
* Increased learning curve
* Create event loop, acquire, crate non-blocking versions of your code
* You think you know Python, there is a second half to learn (async)


Sync vs Async
-------------


Execution
---------


Further Reading
---------------
* Kennedy, M. Demystifying Python's Async and Await Keywords [#Kennedy2019]_
* Kennedy, M. Async Techniques and Examples in Python [#Kennedy2022]_
* Abdalla, A. Creating a Bittorrent Client using Asyncio [#Abdalla2017]_
* Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_


AsyncIO Awaitable
=================
* Since Python 3.5 :pep:`492` -- Coroutines with async and await syntax
* Object is an awaitable if it can be used in an ``await`` expression
* Awaitable objects: Coroutines, Tasks, Futures
* ``__await__`` and ``await`` keyword


Awaitables
----------


Objects
-------


Typing
------


AsyncIO Coroutine
=================
* Coroutine function and coroutine object are two different things
* Coroutine function is the definition (``async def``)
* Coroutine function will create coroutine when called
* This is similar to generator object and generator function
* Coroutine functions are not awaitables
* Coroutine objects are awaitables
* Coroutines declared with the ``async``/``await`` syntax is the preferred way of writing asyncio applications. [#pydocAsyncioTask]_
* https://peps.python.org/pep-0492/


Syntax
------


Coroutine Function
------------------
* Coroutine function is the definition (``async def``)
* Also known as async functions
* Defined by putting ``async`` in front of the ``def``
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``
* Coroutine functions are not awaitables


Coroutine Object
----------------
* Coroutine function will create coroutine when called
* Coroutine objects are awaitables
* To execute coroutine object you can ``await`` it
* To execute coroutine object you can ``asyncio.run()``
* To schedule coroutine object: ``ensure_future()`` or ``create_task()``


Run Sequentially
----------------
* All lines inside of coroutine function will be executed sequentially


Run Concurrently
----------------
* To run coroutine objects use ``asyncio.gather()``
* This won't execute in parallel (won't use multiple threads)
* It will run concurrently (in a single thread)


Error: Created but not awaited
------------------------------
* Created but not awaited objects will raise an exception
* This prevents from creating coroutines and forgetting to "await" on it


Error: Running Coroutine Functions
----------------------------------
* Only coroutine objects can be run
* It is not possible to run coroutine function


Error: Multiple Awaiting
------------------------
* Coroutine object can only be awaited once


Error: Await Outside Coroutine Function
---------------------------------------
* Only a coroutine function (``async def``) can use ``await``
* Non-coroutine functions (``def``) cannot use ``await``


Getting Results
---------------


Inspect
-------


AsyncIO Sleep
=============
* Coroutine ``asyncio.sleep(delay, result=None)``
* Delay can be int or float
* Block for delay seconds.
* If result is provided, it is returned to the caller when the coroutine completes
* Delay is not guaranteed
* It means that this is at least X number of seconds
* This us due, that after that time of delay, there might still be an other function running
* This does not interrupt or preempt


AsyncIO Run
===========
* ``asyncio.run()`` is a main entrypoint
* ``asyncio.gather()`` can run concurrently and gather result (in order of its arguments)


Run Coroutine
-------------
* ``asyncio.run(coro, *, debug=False)``
* Execute the coroutine ``coro`` and return the result
* Takes care of managing the asyncio event loop, finalizing asynchronous generators, and closing the threadpool
* Cannot be called when another asyncio event loop is running in the same thread
* Always creates a new event loop and closes it at the end
* It should be used as a main entry point for asyncio programs, and should ideally only be called once


Run Sequentially
----------------


Run Concurrently
----------------
* awaitable ``asyncio.gather(*aws, return_exceptions=False)``
* Run awaitable objects in the ``aws`` sequence concurrently
* If any awaitable in ``aws`` is a coroutine, it is automatically scheduled as a ``Task``
* If all awaitables are completed successfully, the result is an aggregate list of returned values
* The order of result values corresponds to the order of awaitables in ``aws``
* ``return_exceptions=False`` (default): the first raised exception is immediately propagated to the task that awaits on ``gather()``; other awaitables in the ``aws`` sequence won't be cancelled and will continue to run
* ``return_exceptions=True``: exceptions are treated the same as successful results, and aggregated in the result list
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
* If any ``Task`` or ``Future`` from the ``aws`` sequence is cancelled, it is treated as if it raised ``CancelledError`` – the ``gather()`` call is not cancelled in this case
* This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled


Run as Completed
----------------
* ``asyncio.as_completed(aws, *, timeout=None)``
* Run awaitable objects in the ``aws`` iterable concurrently
* Return an iterator of coroutines
* Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining awaitables
* Raises ``asyncio.TimeoutError`` if the timeout occurs before all Futures are done


Run in Threads
--------------
* coroutine ``asyncio.to_thread(func, /, *args, **kwargs)``
* Asynchronously run function func in a separate thread.
* Any ``*args`` and ``**kwargs`` supplied for this function are directly passed to func.
* Return a coroutine that can be awaited to get the eventual result of func.
* This coroutine function is intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were ran in the main thread.


AsyncIO Wait
============
* ``asyncio.wait(aws, timeout)``
* ``wait()`` - when a timeout occurs: does not cancel the futures
* If aw is a coroutine it is automatically scheduled as a Task
* Returns those implicitly created Task objects in (done, pending) sets


Wait
----
* Coroutine ``asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)``
* ``aws`` must be iterable (list, tuple, set)
* ``aws`` iterable must not be empty
* Run awaitable objects in the ``aws`` concurrently and block until the condition specified by ``return_when``
* ``timeout: float|int`` if specified, maximum number of seconds to wait before returning
* ``wait()`` does not cancel the futures when a timeout occurs
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
* ``return_when`` indicates when this function should return
* ``return_when`` must be one of ``FIRST_COMPLETED``, ``FIRST_EXCEPTION``, ``ALL_COMPLETED``
* ``return_when=FIRST_COMPLETED`` - The function will return when any future finishes or is cancelled;
* ``return_when=FIRST_EXCEPTION`` - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED;
* ``return_when=ALL_COMPLETED`` - The function will return when all futures finish or are cancelled
* Does not raise ``asyncio.TimeoutError``
* ``Futures`` or ``Tasks`` that aren't done when the timeout occurs are simply returned in the second set (``pending``).


AsyncIO Wait For
================
* ``asyncio.wait_for(aw, timeout: int|float|None)``
* Timeout - number of seconds to wait for
* If ``timeout=None``, block until the future completes
* ``wait_for()`` - when a timeout occurs: cancels the task and raises ``asyncio.TimeoutError``
* If aw is a coroutine it is automatically scheduled as a Task
* If the wait is cancelled, the future ``aw`` is also cancelled.


Wait For
--------
* The function will wait until the future is actually cancelled
* Therefore the total wait time may exceed the timeout
* If an exception happens during cancellation, it is propagated
* If coroutine does not finish by then, rises ``TimeoutError``


Handling Timeouts
-----------------


Handling Timeouts Concurrently
------------------------------


Handling Cancellation
---------------------
* If ``gather()`` is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled


Further Reading
---------------
* Langa Ł. How Exception Groups Will Improve Error Handling in AsyncIO [#Langa2022]_


AsyncIO Task
============
* ``asyncio.create_task(coro, *, name=None)``
* Tasks are used to schedule coroutines concurrently
* Wrap the ``coro`` coroutine into a ``Task`` and schedule its execution
* ``Task`` can be used to cancel execution
* ``Task`` can be awaited until it is complete
* The task is executed in the loop returned by ``get_running_loop()``
* ``RuntimeError`` is raised if there is no running loop in current thread
* Tasks are used to run coroutines in event loops
* If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future
* When the Future is done, the execution of the wrapped coroutine resumes
* Manual instantiation of ``Tasks`` is discouraged
* Use the high-level ``asyncio.create_task()`` function to create Tasks


Selected Task Methods
---------------------
* class ``asyncio.Task(coro, *, loop=None, name=None)`` - A Future-like object that runs a Python coroutine. Not thread-safe.
* method ``asyncio.Task.cancel(msg=None)`` - Request the Task to be cancelled. This arranges for a ``CancelledError`` exception to be thrown into the wrapped coroutine on the next cycle of the event loop.
* method ``asyncio.Task.cancelled()`` - Return ``True`` if the ``Task`` is cancelled.
* method ``asyncio.Task.done()`` - Return ``True`` if the ``Task`` is done.
* method ``asyncio.Task.result()`` - Return the result of the ``Task``. If the result isn't yet available, raise ``InvalidStateError``.
* method ``asyncio.Task.exception()`` - Return the exception of the ``Task``
* method ``asyncio.Task.add_done_callback(callback, *, context=None)`` - Add a callback to be run when the ``Task`` is done.
* method ``asyncio.Task.remove_done_callback(callback)`` - Remove callback from the callbacks list.
* method ``asyncio.Task.set_name(value)`` - Set the name of the ``Task``.
* method ``asyncio.Task.get_name()`` - Return the name of the ``Task``.


Introspection
-------------
* ``asyncio.current_task(loop=None)`` - Return the currently running Task instance, or None if no task is running.
* ``asyncio.all_tasks(loop=None)`` -  Return a set of not yet finished Task objects run by the loop.
* If loop is ``None``, ``get_running_loop()`` is used for getting current loop.


AsyncIO Future
==============
* Low-level awaitable object
* Represents an eventual result of an asynchronous operation
* Normally there is *no need* to create Future objects at the application level code
* When a ``Future`` object is awaited it means that the coroutine will wait until the ``Future`` is resolved in some other place
* Future objects in asyncio are needed to allow callback-based code to be used with ``async``/``await``


AsyncIO Shield
==============
* Shielding from Cancellation
* Awaitable ``asyncio.shield(aw)``
* Protect an awaitable object from being cancelled.


AsyncIO Debug
=============
* By default asyncio runs in production mode
* Asyncio has a debug mode which can be enabled
* More verbose message you can achieve by using ``PYTHONASYNCIODEBUG=1`` and ``PYTHONTRACEMALLOC=1`` environment variables
* Also ``python3 -X dev -X tracemalloc=5 myfile.py``


Debug
-----
* By default asyncio runs in production mode
* Asyncio has a debug mode which can be enabled


Introspection
-------------
* ``asyncio.current_task(loop=None)`` - Return the currently running Task instance, or None if no task is running.
* ``asyncio.all_tasks(loop=None)`` -  Return a set of not yet finished Task objects run by the loop.
* If loop is ``None``, ``get_running_loop()`` is used for getting current loop.


Further Reading
---------------
* https://docs.python.org/3/library/devmode.html
* https://docs.python.org/3/library/asyncio-dev.html#debug-mode


AsyncIO Event Loop
==================
* Async code can only run inside an event loop.
* The event loop is the driver code that manages the cooperative multitasking.
* You can create multiple threads and run different event loops in each of them.
* Python will create a default event loop only in Main Thread
* Python will not create an event loop automatically for you on any other than main thread by default, this is to prevent from having multiple event lops created explicitly
* Event loop can execute only one callback (coroutine) at a time
* Some callbacks (coroutines) can schedule themselves once again (trampoline)
* Reactors
* Proactors


Selectors
---------


Loop
----


UVLoop
------
* The ultimate loop implementation for UNIXes (run this on production)


AsyncIO Queue
=============
* ``asyncio`` queues are designed to be similar to classes of the ``queue`` module.
* Although ``asyncio`` queues are not thread-safe, they are designed to be used specifically in async/await code.
* Note that methods of asyncio queues don't have a timeout parameter; use`` asyncio.wait_for()`` function to do queue operations with a timeout.


FIFO Queue
----------
* FIFO Queue - First In, First Out
* class ``asyncio.Queue(maxsize=0)``
* If maxsize is less than or equal to zero, the queue size is infinite.
* Unlike the standard library threading queue, the size of the queue is always known and can be returned by calling the qsize() method.
* ``maxsize`` - Number of items allowed in the queue.
* ``empty()`` - Return True if the queue is empty, False otherwise.
* ``full()`` - Return True if there are maxsize items in the queue.
* coroutine ``get()`` - Remove and return an item from the queue. If queue is empty, wait until an item is available.
* ``get_nowait()`` - Return an item if one is immediately available, else raise QueueEmpty.
* coroutine ``join()`` - Block until all items in the queue have been received and processed.
* coroutine ``put(item)`` - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* ``put_nowait(item)`` - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* ``qsize()`` - Return the number of items in the queue.
* ``task_done()`` - Indicate that a formerly enqueued task is complete.


Priority Queue
--------------
* class ``asyncio.PriorityQueue``
* Retrieves entries in priority order (lowest first).
* Entries are typically tuples of the form (priority_number, data).


LIFO Queue
----------
* LIFO Queue - Last In, First Out
* class ``asyncio.LifoQueue``
* Retrieves most recently added entries first.


Exceptions
----------
* exception ``asyncio.QueueEmpty`` - Raised when ``get_nowait()`` method is called on an empty queue.
* exception ``asyncio.QueueFull`` - Raised when ``put_nowait()`` method is called on a queue that has reached its maxsize.


AsyncIO Stream
==============


AsyncIO Synchronization
=======================
* Synchronization Primitives
* Mutex Lock
* Condition Object
* Semaphore
* Event


Mutex Lock
----------
* Class ``asyncio.Lock()``
* Can be used to guarantee exclusive access to a shared resource
* Not thread-safe.


Condition Object
----------------
* class ``asyncio.Condition(lock=None)``
* Not thread-safe.


Semaphore
---------
* class ``asyncio.Semaphore(value=1)``
* Manages an internal counter which is decremented by each ``acquire()`` call and incremented by each ``release()`` call.
* The counter can never go below zero.
* When ``acquire()`` finds that it is zero, it blocks, waiting until some task calls ``release()``.


Event
-----
* class ``asyncio.Event()``
* Can be used to notify multiple asyncio tasks that some event has happened.
* coroutine ``wait()`` - Wait until the event is set. If the event is set, return ``True`` immediately. Otherwise block until another task calls ``set()``.
* ``set()`` - Set the event. All tasks waiting for event to be set will be immediately awakened.
* ``clear()`` - Clear (unset) the event. Tasks awaiting on ``wait()`` will now block until the ``set()`` method is called again.
* ``is_set()`` - Return ``True`` if the event is set.


AsyncIO Iterator
================
* Asynchronous Generators https://peps.python.org/pep-0525/
* Asynchronous Comprehensions https://peps.python.org/pep-0530/
* ``__aiter__``
* ``__anext__``


Typing
------
* ``collections.abc.AsyncGenerator``


AsyncIO Iterator
================
* Asynchronous Generators https://peps.python.org/pep-0525/


Typing
------
* ``collections.abc.AsyncGenerator``


AsyncIO Comprehensions
======================
* Asynchronous Comprehensions https://peps.python.org/pep-0530/


Recap
-----


AsyncIO Context Manager
=======================
* ``__aenter__``
* ``__aexit__``


AsyncIO 3rd Party
=================


Unsync
------
* Library decides which to run, thread, asyncio or sync


Twisted
-------
* Old project


Gevent
------
* Actively maintained
* Greenlets (micro-threads running inside one thread)


Tornado
-------
* Actively maintained
* Web framework and asynchronous networking library
* Open-sourced by Facebook after acquisition of FriendFeed


Curio
-----
* Coroutine-based library for concurrent Python systems programming
* Provides standard programming abstractions such as tasks, sockets, files, locks and queues
* Works on POSIX and Windows


Trio
----
* Python library for async concurrency and I/O
* Focussed on usability and correctness
* Introduced nursery (task groups)


UVLoop
------
* The ultimate loop implementation for UNIXes (run this on production)
