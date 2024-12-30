import string


def first_word(text):
    """
    Extracts the first valid word from the given text. A word begins with an
    ASCII letter and may include an apostrophe provided it is positioned
    after the initial ASCII letter(s). The function stops capturing the word
    upon encountering a non-valid character, excluding the starting set of
    valid criteria.

    :param text: The input string from which the first word needs to
        be extracted.
    :type text: str
    :return: The first valid word found in the input string following
        the specified word-validity rules. Returns an empty string if no
        valid word is found.
    :rtype: str
    """
    start = False
    word = ""

    for char in text:
        if char in string.ascii_letters or (char == "'" and start == True):
            start = True
            word += char
            continue
        else:
            if start:
                break

    return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
