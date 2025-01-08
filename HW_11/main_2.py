from typing import Generator
from inspect import isgenerator


def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Generates cube numbers starting from the cube of 2 up to a specified limit.

    This generator function computes cube numbers starting at 2**3 (8) and yields
    cubes iteratively as long as the cube is less than or equal to the specified
    limit. It stops generating once a cube exceeds the `end` limit.

    :param end: Upper limit for generating cube numbers. Cube values generated
                will be less than or equal to this value.
    :type end: int
    :return: A generator of cube numbers from the cube of 2 up to `end`.
    :rtype: Generator[int, None, None]
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
