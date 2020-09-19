---
title: Decorators
author: Gautham K
---

<center>

    <p>
        <i>
            If you can't explain it simple enough, you don't understand it well enough! - <strong>Albert Einstein</strong>
        </i>
    </p>

</center>

Since the time I incepted programming with Python, I've come across the term "Decorators" at least "m" times and tried understanding them at least "n" times. Where, 

> "m" &#8712; values > 100 &#38; , 

> "n" &#8712; values > 10 !

I learnt the concept quite a few times but never could remember. Lately, once again, I realised I don't remember it anymore again and then thought, maybe I don't understand it in the first place and thought of learning it again. But this time, I decided to explain what I understand of it, provided, I understand it in the first place &#129322; .

Let's try understanding it by breaking the concept into the following topics:

* Defining a decorator
* Creating a decorator
* Calling a decorator

Therefore, let's jump directly, not into conclusions but into the concept.

### Defining a Decorator

_Definition :_ (simply put) A decorator, is a function, that is used to, tweak the functionality(s), of another function.

(Well defined, right? A definition just as good as any other Greek or Latin movie that we've watched recently, isn't it?)

No worries, let's break it further. From the definition above, we can be sure that, 

1. All that a decorator is involved is _functions_. isn't it?

2. A decorator is itself just a _function_. (Nice, very good! very good!!)

3. A decorator, is a _function_, that accepts a _function_ as an argument and returns a _function_.

After realising the 3rd point above, that first thought that stuck my mind was, "So, it the capability of being '_first-class_ objects' that is the _culprit_."

Anyways, let's try turning the human readable text above into machine (or, Python virtual machine, to be precise) readable text as follows.

### Creating a Decorator

Consider the following statement:

> let's have a function, called as `summer` (sum'mer, &#128540; ), used to _sum_ the arguments given to it, as follows

``` python

# summer : a function that sums it's arguments

def summer(a, b):
    return a + b
```

By the signature of the above function, it is sure that it returns a, 

* integer if integers are passed as arguments

* float if floats are passed as arguments

However, I want the `summer` function to return float values even if its arguments are integers but don't want to change the it's signature.

> Decorators to the rescue, let's create a decorator, that could convert any numeric arguments given to a function, into float values.

the definition of such a decorator would look something like the following:

``` python

def float_decorator(arg_func):

    def other_function(p, q):

        return arg_func(float(p), float(q))

    return other_function

```

As discussed earlier, 

* a decorator is just a _function_, in our case `float_decorator` (1st line in code block above)
* the _decorator function_ accepts another _function_ as an argument, in our case `arg_func` => `arg_func` is just a local variable, within the scope / namespace of `float_decorator` , that will be referring to a function passed as an argument
* the decorator must host the definition for another _function_ (here, `other_function` ) (2nd line in code block above), which actually modifies the functionality of the function that is referred by `arg_func` (3rd line in the code block above)
* the function that is defined in the _decorating function ( `float_decorator` )_ , has to be called by the _decorating function_ itself, which here case is, `other_function` (4th line in the code block above)

> Stop, Go back, Understand & Proceed!

### Calling a Decorator

At the end of the day, even a _decorator_ is a _function_, isn't it?

=> even it has to be `called` if it has to be put to work, how to do so?

Calling the decorator function can be done in 2 ways:

* Type 1 : By passing a function, as an argument to the decorating function

* Type 2 : By calling the decorators in a more simpler or usual syntax, provided by Python

#### Type 1 : Passing a function, as an argument

``` python

# summer : a function that sums it's arguments

decorated_summer = float_decorator(summer)

result = decorated_summer(5,6)

print(result)

# output

11.0 # Float value
```

In the first line of the code block above, the _function_ `summer` is being passed as an argument to the _decorating function_ ( `float_decorator` )

=> the identifier `result` now points to decorated_summer() function, that modifies the arguments and and pass them to the function, resulting in _float values_.

The advantage which such special function is, just like any function, they are reusable.

Therefore, let's examine, how to call/invoke a decorator in another way.

#### Type 2 : A more simpler / usual syntax as provided by Python

This way of calling a decorator, the decorator name, with an ' &#64; ', should preceed the actual function definition, as follows.

``` python

# summer : a function that sums it's arguments
@float_decorator
def summer(a, b):
    return a + b

# producer : a function that finds the product of it's arguments
@float_decorator
def producer(a, b):
    return a * b
```

This way, one can simply define their functions and add a decorator as and when required.

Let's check the output of the calling of such functions.

``` python
x = summer(3, 5)

print("x : ", x)
```

**Output**

``` bat
[Running] python -u "c:\Users\~\rough.py"
x :  8.0

[Done] exited with code=0 in 0.343 seconds
```

``` python
y = producer(3, 5)

print("y : ", y)
```

**Output**

``` bat
[Running] python -u "c:\Users\~\rough.py"
y :  15.0

[Done] exited with code=0 in 0.512 seconds
```
