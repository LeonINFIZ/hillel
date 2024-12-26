def second_index(text, some_str):
    """
    Finds the index of the second occurrence of a substring in the text.

    Parameters:
    text (str): The input text.
    some_str (str): The substring for which the second occurrence is to be found.

    Returns:
    int or None: The index of the second occurrence of the substring in the text.
                 If the substring appears less than twice, returns None.
    """
    try:
        return text.index(some_str, text.index(some_str) + 1)
    except ValueError:
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('OK')
