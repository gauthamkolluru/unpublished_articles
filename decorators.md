---
title: Decorators
author: Gautham K
---

Since the time I incepted working with Python, I've come across the term "Decorators" at least "m" times and tried learning them "n" times. Where, 

> "m" &#8712; values > 100 &#38; , 

> "n" &#8712; values > 10 !

So this time, I decided to write an article, explaining what I understand of it, provided, I understand it in the first place &#129322; .

And so, let's jump directly, not into conclusions but into concept.

Let's try understanding it by breaking the concept into the following topics:

* Defining a decorator
* Creating a decorator
* Calling a decorator

### Defining a Decorator

_Definition :_ (simply put) A decorator, is a function, that is used to, tweak the functionality(s), of another function.

Well defined, right? A definition as good as any other Greek or Latin movie that we've watched recently, isn't it?

No worries, let's break it further.

1. From the definition above, we're sure that all decorators involve is _functions_. isn't it?

2. A decorator also, is nothing but a _function_. (Nice, very good very good)

3. A decorator, is a function, that accepts a function as an argument and returns a function.

After realising the 3rd point above, that first thought that stuck my mind was, "So, it the capability of '_first-class_ objects' that is the _culprit_."

Anyways, let's try turning the human readable language above into machine (or, Python virtual machine, to be precise) readable language.

### Creating a Decorator

Consider the following statement:

> Create a decorator, that could convert the given numeric arguments to a function, into floating point values and then execute the function.

the definition of such a decorator should look something like the following code block.

``` python

def float_decorator(arg_func):

    def other_function(*args):

        arg_func([float(i) for i in args])

    return other_function

```

Analysis of the code above:

* `float_decorater` is a function that takes a function as an argument, which is denoted by the parameter `arg_func` .
* The function `float_decorater` 's definition contains the definition another function called as, `other_function` which is being called by the `float_decorater` function.
* This `other_function` , that is defined in the function definition of `float_decorater` is converting the arguments to the `arg_func` into float with the help of this list comprehension `[float(i) for i in args]` .

I hope, things seem as clear as a thick monsoon cloud, right? 

Never mind, let's consider the following functions for which the functionalities has to be tweaked and during the process, re-examine how a python interpreter would interpret it.

### Calling a Decorator

But to do so, we've look at how to use this decorator.

After all, even a _ `decorator` _ is nothing but a _ `function` _, isn't it?

=> even it has to be `called` if it has to be put to work.

Calling the decorator functions can be done in 2 ways:

* Type 1 : By passing the regular function that we have created, as an argument to the decorating function

* Type 2 : By calling the decorators in a more simpler or usual way, provided by Python

> For the purpose of understanding this, lets first create 2 simple functions, one for getting the _sum of arguments_ and other for getting the _product of arguments_, as below.

``` python

# summer : a function that sums it's arguments

def summer(*args):
    return sum(args)

# producer : a function that find the product of it's arguments

def producer(*args):
    prod = 1
    for arg in args:
        prod *= arg
    return prod
```

=> Lets assume that we want the above `summer` () and `producer` functions to return _floating_ values, even if they were provided with _integer_ arguments.

To do so, all we require to do is to add a line just before each function's definition, as follows

> The line to add : @decorator_function ('@' followed by the 'decorator name') as follows

``` python

# summer : a function that sums it's arguments
@decorator_function
def summer(*args):
    return sum(args)

# producer : a function that find the product of it's arguments
@decorator_function
def producer(*args):
    prod = 1
    for arg in args:
        prod *= arg
    return prod
```
