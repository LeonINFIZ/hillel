def is_even(digit: int) -> bool:
    """
    Checks if a given integer is even.

    This function determines whether the provided integer is evenly divisible
    by 2. It returns True if the number is even and False otherwise.

    :param digit: The integer to check for evenness.
    :type digit: int
    :return: Returns True if the given integer is even, otherwise False.
    :rtype: bool
    """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
