from inspect import isgenerator


def generate_cube_numbers(end):
    """
    Generate cube numbers up to a specific limit.

    This function generates the cubes of numbers starting from 2 up to a given limit.
    Cubes are generated for numbers such that the cube value is less than or equal
    to the specified limit. The function employs a generator for yielding each cube
    value instead of returning a precomputed list, thereby optimizing memory usage
    for large ranges.

    :param end: The upper limit (inclusive) up to which cube numbers are generated.
                Must be an integer.
    :return: A generator yielding cube numbers that satisfy the specified limit.
    """
    
    for num in range(2, end + 1):
        if num ** 3 > end:
            return
        else:
            yield num ** 3


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("OK")
