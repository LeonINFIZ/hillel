import string


def correct_sentence(text):
    """
    Adjusts the string so it starts with an uppercase letter
    and ends with a period.

    Parameters:
    text (str): The input string.

    Returns:
    str: A string starting with an uppercase letter and ending with a period.
    """
    text = text[0].upper() + text[1:]

    if text[-1] not in string.ascii_letters:
        text = text[:-1] + "."
    else:
        text = text + "."

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('OK')
