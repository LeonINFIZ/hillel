def second_index(text, some_str):
    """
    Знаходить індекс другого входження підрядка в тексті.

    Параметри:
    text (str): Початковий текст.
    some_str (str): Підрядок, для якого потрібно знайти друге входження.

    Повертає:
    int або None: Індекс другого входження підрядка в тексті.
                  Якщо підрядок зустрічається менше двох разів, повертає None.
    """
    try:
        return text.index(some_str, text.index(some_str) + 1)
    except ValueError:
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
