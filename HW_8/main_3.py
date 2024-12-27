def find_unique_value(some_list):
    """
    Finds and returns the first unique (non-repeating) value in the given list.

    This function iterates through the given list and checks the count of each element.
    The first element that appears exactly once is returned.

    Args:
        some_list (list): A list of elements (integers, floats, or other hashable types)
                          where at least one unique value is guaranteed to exist.

    Returns:
        Any: The first unique value found in the list.
    """
    for value in some_list:
        if some_list.count(value) == 1:
            return value


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
