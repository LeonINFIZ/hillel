def is_even(number):
    """
    Determine if a given number is even.

    This function checks whether the given number is even by evaluating the last
    digit of its string representation and comparing it to the set of digits
    representing even numbers (0, 2, 4, 6, 8).

    :param number: The number to check for evenness.
    :type number: int
    :return: True if the number is even, False otherwise.
    :rtype: bool
    """
    return True if str(number)[-1] in "02468" else False


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('OK')
