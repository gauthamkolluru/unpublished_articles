def float_decorator(arg_func):

    def other_function(p, q):

        return arg_func(float(p), float(q))

    return other_function


@float_decorator
def summer(a, b):
    return a + b


@float_decorator
def producer(a, b):
    return a * b


# x = summer(3, 5)

# print("x : ", x)

y = producer(3, 5)

print("y : ", y)


# def another_float_decorator(p, q):

#     def other_function(arg_func):

#         return arg_func(float(p), float(q))

#     return other_function


# y = another_float_decorator(summer)

# print("y : ", y(3, 5))
