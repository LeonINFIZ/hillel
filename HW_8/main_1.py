def add_one(some_list):
    """
    Increments the integer represented by a list of digits by 1 and returns the resulting list of digits.

    This function assumes that the input list contains only non-negative single-digit integers (0-9) and
    represents a non-negative integer. The digits are ordered such that the most significant digit is
    the first element of the list.

    Args:
        some_list (list of int): A list of single-digit integers representing a non-negative number.

    Returns:
        list of int: A new list of digits representing the input number incremented by 1.

    Edge cases:
        - If the list contains a single 9, e.g., [9], the result will be [1, 0].
        - If the input is all 9s, e.g., [9, 9, 9], it will correctly handle the carry over and return [1, 0, 0, 0].
    """

    number = ""
    for digit in some_list:
        number += str(digit)
    number = int(number) + 1
    return [int(digit) for digit in str(number)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
