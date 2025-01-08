from inspect import isgenerator


def prime_generator(end):
    """
    Generates prime numbers up to a specified limit.

    This function is a generator that yields prime numbers from 2 to the given
    endpoint (inclusive). It evaluates each number in the range using the
    trial division method, checking if the number is evenly divisible by any
    of the integers between 2 and the square root of the number (inclusive).
    If a number is not divisible by any of these, it is classified as prime
    and yielded as part of the sequence.

    :param end: The upper limit of the range to generate primes (inclusive).
    :type end: int
    :return: A generator yielding prime numbers within the specified range.
    :rtype: Iterator[int]
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
