---
title: Decorators
author: Gautham K
---

Since the time I incepted working with Python, I've come across the term "Decorators" at least "m" times and tried learning them "n" times. Where, 

> "m" &#8712; values > 100 &#38; , 

> "n" &#8712; values > 10 !

So this time, I decided to write an article, explaining what I understand of it, provided, I understand it in the first place &#129322; .

And so, let's jump directly, not into conclusions but into concept.

_Definition :_ (simply put) A decorator, is a function, that is used to, tweak the functionality(s), of another function.

Well defined, right? A definition as good as any other Greek or Latin movie that we've watched recently, isn't it?

No worries, let's break it further.

1. From the definition above, we're sure that all decorators involve is _functions_. isn't it?

2. A decorator also, is nothing but a _function_. (Nice, very good very good)

3. A decorator, is a function, that accepts a function as an argument and returns a function.

After realising the 3rd point above, that first thought that stuck my mind was, "So, it the capability of '_first-class_ objects' that is the _culprit_."

However, let's try turning the human readable language above into machine (or, Python virtual machine, to be precise) readable language.

Consider the following problem statement, 

Create a decorator, that could convert the given numeric arguments to a function, into floating point values and then execute the function.

the definition of such a decorator should look something like the following code block.

``` python

def decorator_function(arg_func):

    def other_function(*args):

        arg_func([float(i) for i in args])

    return other_function

```

Now, let's consider the following functions for which the functionalities has to be tweaked.

``` python

# example for "addition" function

def addition(*args):
    return sum(args)

# example for "multiplication" function

def multiplication(*args):
    mul = 0
    for arg in args:
        mul *= arg
    return mul
```

=> Lets assume that we want the above functions to return _floating_ values, even if they were provided with _integer_ arguments.

To do so, all we require to do is to add a line just before each function's definition, as follows

> The line to add : @decorator_function ('@' followed by the 'decorator name') as follows

``` python

# example for "addition" function
@decorator_function
def addition(*args):
    return sum(args)

# example for "multiplication" function
@decorator_function
def multiplication(*args):
    mul = 0
    for arg in args:
        mul *= arg
    return mul
```

