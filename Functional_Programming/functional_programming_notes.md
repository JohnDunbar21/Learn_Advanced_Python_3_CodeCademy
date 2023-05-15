# Functional Programming in Python 3

**Functional programming structures code in such a way that it is primarily composed of functions, and is distinctly different from Object-Oriented Programming**.

## Functional vs. OOP

In OOP, code is based on the concept of **objects**, creating templates using the keyword `class`. Objects contain fields that store data and methods to manipulate the data.

In functional programming, code is built using primarily **functions**, who have a *first-class citizen* priority, meaning they can store and manipulate data - with some limitations. Similar to OOP, functional programming allows functions to be passed as arguments into other funtions and can also be returned by other functions.

## Declarative vs. Imperative Programming

**Imperative Programming** solves a problem by describing the step-by-step solution: *how to solve the problem*.

**Declarative Programming** relies on the framework or programming language to solve a problem: *what problem to solve*.

Imperative code is generally easier to read and understand, but often yields longer production time. Ultimately what should determine which style of code is used is the end-goal(s) of the programmer in question.

OOP and procedural programming follow the **imperative approach** where functional programming follows  the **declarative approach**.

## Writing Functions in Functional Programming

The first requirment for a program to follow functional programming is that is *must* be deterministic: that is, for any given input, the function must return the same output when provided with the same set of inputs. This is illustrated in the following `add` function.

```py
"""
Returns the sum of two integer values
"""
def add(x: int, y: int):
    return x + y
```

The `add` function will *always* return `7` if `add(5, 2)` is called, thus fulfilling the deterministic requirment.

Another requirment for a program to follow functional programming is that it *must* be free of as many **side effects** as possible - a side effect being the event where a function alters an external variable. The goal is to *minimise* not eliminate side effects.

A **pure function** is a deterministic function with no side effects. The `add` function above is an example of a pure function as it neither accesses nor manipulates any external variables, only operating within its own scope.

Pure functions are extremely important in order to preserve maintainability as the program continues to grow. Having a function that is not dependent on any external factors also makes it more versatile/reusable.

## Using Recursion Instead of Loops

Since loops do not adhere to the functional programming style - because they maintain an external counter which is altered from inside the loop, which is considered a side effect - recursion is used to repeat code. An example of a recursive function is the Fibonacci sequence below.

```py
"""
Returns the n-th Fibonnaci number using recursion
"""
def fibonnaci_number(number : int):
    if number <= 1:
        return 1
    return fibonnaci_number(number - 1) + fibonnaci_number(number - 2)
```

## Passing Functions as Arguments to Other Functions

In OOP, objects can be passed as arguments to functions, and in functional programming, functions can be passed as arguments to other functions. This is known as treating functions as *first-class citizens*. An example of this trait is shown in the code sample below.

```py
"""
Returns the sum of two integer values
"""
def add(x: int, y: int):
    return x + y

"""
Returns the difference of two integer values
"""
def sub(x: int, y: int):
    return x - y

"""
Returns the product of some returned value of another function on two integer values
"""
def function_product_3(a: int, b: int, function: object):
    return 3 * function(a, b)

add_and_times_3 = function_product_3(2, 4, add) # Will return 18
sub_and_times_3 = function_product_3(2, 4, sub) # Will return -6
```

Functional programming promotes brevity when writing code in order to maintain readability. This can be achieved through the use of `lambda` functions. Using the same functionality as the above code sample, it can be rewritten using lambdas as follows.

```py
"""
Returns the product of some returned value of another function on two integer values
"""
def function_product_3(a: int, b: int, function: object):
    return 3 * function(a, b)

add_and_times_3 = function_product_3(2, 4, lambda x, y: x + y) # Will return 18
sub_and_times_3 = function_product_3(2, 4, lambda x, y: x - y) # Will return -6
```

The above code sample will produce the same outputs as its predecessor, but results in a more concise structure. However, `lambda` functions are only suitable for implementing *simple* functions, i.e., simple logic functions.