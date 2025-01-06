from inspect import isgenerator


def pow(x):
    """
    Calculate the square of a given number.

    This function computes the square of the input value `x` and returns it.
    It supports any numeric type, including floating-point and integer values.

    :param x: The number to be squared.
    :type x: int or float
    :return: The square of the input number `x`.
    :rtype: int or float
    """
    return x ** 2


def some_gen(begin, end, func):
    """
    A generator function that iteratively produces values starting from `begin`, applying the `func`
    transformation to the current value until the specified `end` value is reached. The generator yields
    the current value of `begin` in each iteration.

    :param begin: The starting value of the sequence.
    :type begin: int
    :param end: The limit value upon which the iteration stops. The iteration continues as long
        as the current value is less than this limit.
    :type end: int
    :param func: A callable function that takes the current value as input and transforms it to
        the next value in the sequence.
    :type func: callable
    :return: Yields successive values of `begin` as transformed by `func`.
    :rtype: generator
    """

    for i in range(end):
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
