# Concurrent Programming in Python

## Python `threading` Module

A *thread* is a unique flow of execution: theoretically, multiple threads mean having the ability to run multiple things at the same time. In Python, threads do not run simultaneously, even though they appear to do so, however it is still much faster to make use of threads in a given program.

To create a thread instance in Python:

```py
import threading
new_thread = threading.Thread(target=some_function, args=(some_arg,))
```

The two most important parameters when initialising a thread are:
- **target** : the function to be executed, default = `None`
- **args** : the argument(s) to be applied to the function, default = `None`

After creating a thread instance, it has to run using:

```py
new_thread.start() # Begins the execution process of the thread
```

## Using Multiple Threads in Python

Examine the following code:

```py
threads = [] # Will store all of the threads to execute
args = [arg1, arg2, arg3] # Stores all the arguments to use

for arg in range(len(args)):

    thread = threading.Thread(target=some_function, args=(args[arg],))

    threads.append(thread) # Add the thread to the multithreading list

    thread.start() # Begin the execution process
```

This shows a rudimentary method of multithreading.

## Joining a Thread

We can use the `join()` method to tell one thread to wait for another thread to stop before moving on. For example:

```py
import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(string + " says hello!")


def main_threading():
  s = time.perf_counter()
  threads = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  for i in range(len(greetings)):
    t = threading.Thread    (target=greeting_with_sleep, args=(greetings[i],)) 
    t.start()
    
    threads.append(t)
  
  for thread in threads:
    thread.join()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

main_threading()
```

## Python `asyncio` Module

The `asyncio` module uses `async` and `await` syntax/keywords that allow you to build and execute asynchronous code in programs.

The `async` keyword declares a function as a *coroutine* - a function that may return normally with a value or may suspend themselves internally and return a continuation. In other words, tasks can be paused and resumed to mimic multithreading.

The `await` keyword suspends the execution of the current task until whatever is being awaited is completed.

```py
import time
import asyncio

async def greeting_with_sleep_async(string):
  s = time.perf_counter()
  print(string)
  await asyncio.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

"""
Older Syntax < 3.7
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(greeting_with_sleep_async("Codecademy"))

"""
Newer Syntax > 3.7
"""
asyncio.run(greeting_with_sleep_async("Codecademy"))
```

## Multiple Asynchronous Tasks

Consider the following code:

```py
import time
import asyncio

async def greeting_with_sleep_async(string):
  print(string)
  await asyncio.sleep(2)
  print(string + " says hello!")


async def main_async():
  s = time.perf_counter()
  greetings = [greeting_with_sleep_async('Codecademy'), greeting_with_sleep_async('Chelsea'), greeting_with_sleep_async('Hisham'), greeting_with_sleep_async('Ashley')]
  await asyncio.gather(*greetings)

  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
```

## Python `multiprocessing` Module

The `multiprocessing` module allows parallelism to take place, leveraging multiple CPUs to execute tasks. In terms of code syntax, it appears very similarly to how `threading` is done.

Examine the following code:

```py
import time
import multiprocessing

def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

p = multiprocessing.Process(target=greeting_with_sleep, args=("Codecademy",))
p.start()
```

## Using Multiple Processes

```py
import time
import multiprocessing

def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print(string + " says hello!")


def main_multiprocessing():
  s = time.perf_counter()
  processes = []
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  
  for i in range(len(greetings)):
    p = multiprocessing.Process(target=greeting_with_sleep, args=(greetings[i],))
    processes.append(p)
    p.start()

  for j in processes:
    j.join()
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

main_multiprocessing()
```