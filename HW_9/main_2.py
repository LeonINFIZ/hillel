def difference(*args):
    """
    Calculates the difference between the largest and smallest values in the given argument list.
    Supports integer and float types and returns the result rounded to two decimal places
    for float values.

    :param args: Variable length argument list of numbers to calculate the difference between.
        Must only contain numeric types (integers or floats).
    :return: The difference between the largest and smallest numbers in the argument list.
        If the list is empty, returns 0. If the largest and smallest values are floats,
        the result will be rounded to 2 decimal places.
    """
    args = list(args)

    if not args:
        return 0

    args.sort()

    if type(args[-1]) == float and type(args[0]) == float:
        return round(args[-1] - args[0], 2)
    else:
        return args[-1] - args[0]


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
