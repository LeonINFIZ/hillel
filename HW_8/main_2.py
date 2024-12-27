import string

punctuation = set(string.punctuation)
punctuation.add(' ')


def is_palindrome(text):
    """
    Checks whether the given text is a palindrome.

    A palindrome is a word, phrase, or sequence of characters that reads the same
    backward as forward, ignoring case, spaces, and punctuation.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the text is a palindrome, otherwise False.

    Notes:
        - Punctuation marks and spaces are ignored.
        - The check is case-insensitive.
    """

    text = text.lower()
    new_text = ""
    for symbol in text:
        if symbol not in punctuation:
            new_text += symbol
    for symbol in range(len(new_text) // 2):
        if new_text[symbol] != new_text[-symbol - 1]:
            return False
    else:
        return True


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
