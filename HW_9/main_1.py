def popular_words(text, words):
    """
    Calculates the frequency of specific words within a given text.

    This function takes a block of text and a list of words as input.
    It evaluates how many times each word from the list appears in
    the provided text. The function returns a dictionary where the
    keys are the given words and the values represent their respective
    occurrences in the text. Words are matched case-insensitively.

    :param text: The text in which word occurrences will be counted.
                 The text is expected as a single string.
    :type text: str
    :param words: A list of words to search for within the text. Each
                  word's frequency will be determined.
    :type words: list[str]
    :return: A dictionary mapping each word from the input list to the
             number of times it occurs in the text.
    :rtype: new_dict[str, int]
    """
    text = text.lower()
    text = text.split()

    new_dict = {}
    for word in words:
        if word in text:
            new_dict[word] = text.count(word)
        else:
            new_dict[word] = 0
    return new_dict


assert popular_words('''When I wAs One I had just begun When I waS Two I WAS nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
