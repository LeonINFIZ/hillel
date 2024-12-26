def second_index(text, some_str):
    try:
        return  text.index(some_str, text.index(some_str) + 1)
    except ValueError:
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
