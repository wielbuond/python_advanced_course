

Threading About
===============
* Zaletą wątków jest to, że mają współdzielony stan
* Jeden wątek może zapisać kod do pamięci a drugi odczytać bez narzutu komunikacyjnego
* Wadą jest również współdzielony stan i race condition
* Ideą wątków jest tani dostęp do współdzielonej pamięci, tylko trzeba wszędzie wstawiać locki
* Run very fast, but hard to get correct
* It's insanely difficult to create large multi-threaded programs with multiple locks
* Even if you lock resource, there is no protection if other parts of the system do not even try to acquire the lock
* Threads switch preemptively
* Preemptively means that the thread manager decides to switch tasks for you (you don't have to explicitly say to do so). Programmer has to do very little.
* This is convenient because you don't need to add explicit code to cause a task switch
* The cost of this convenience is that you have to assume a switch can happen at any time
* Accordingly, critical sections have to be a guarded with locks
* The limit on threads is total CPU power minus the cost of tasks switches and synchronization overhead
* Why Should Async Get All The Love Advanced Control Flow With Threads [#Davis2022]_


Frequently Asked Questions
--------------------------


Daemon
------
* https://stackoverflow.com/a/190017/228517


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


Thread-safety
-------------
* Thread-safe code is code that will work even if many Threads are executing it simultaneously.


Threading Timer
===============


Delay execution
---------------
* dlaczego nie ``time.sleep()``
* rekurencyjny timer


Threading Queues
================
* Queue
* FIFO
* LIFO (stack)
* Priority Queue
* Priorytetyzacja
* Wywłaszczenie
* Network Queue
* Synchronizacja
* Routing


Standard Library
----------------
* ``queue``


Threading Create
================


Threading Synchronization
=========================
* Thread Synchronisation


Problems
--------
* Lock Contention - when there is a shared resource which is wanted by many threads very often. Most of the threads will wait for access to that resource
* Lock Starvation - some threads are more lucky to get more access than the others. There are even some threads which didn't get a lock at all!
* Deadlock - You cannot access a lock to get a resource, because you haven't acquired a resource in the first place (example: the pharmacy won't sell you mask, because you are not wearing a mask)
* The more lock, the slower your program is and more memory it uses


Locks
-----
* Locks don't lock anything. They are just flags and can be ignored. It is a cooperative tool, not an enforced tool
* IIn general, locks should be considered a low level primitive that is difficult to reason about nontrivial examples. For more complex applications, you're almost always better of with using atomic message queues.
* The more locks you acquire at one time, the more you loose the advantages of concurrency


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


Thread Local Storage
--------------------
* Operating system mechanism
* Limits global variables to be seen only by current thread
* You can keep data around, which are specifically not shared with other threads


Threading Join
==============


Threading Worker
================


Workers
-------
