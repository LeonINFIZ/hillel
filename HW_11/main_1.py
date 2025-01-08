from inspect import isgenerator


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Generates prime numbers up to the specified limit.

    This function is a generator that yields prime numbers one by one, starting
    from 2, up to the specified 'end' value. It uses an efficient algorithm
    to check the primality of a number by iterating only up to the square root
    of the number. Each number that satisfies the conditions for being a prime
    is yielded.

    :param end: The upper limit up to which prime numbers are generated. The
        function includes 'end' if it is a prime number.
    :type end: int
    :return: A generator that yields prime numbers up to the specified limit.
    :rtype: Generator[int, None, None]
    """

    for num in range(2, end + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
