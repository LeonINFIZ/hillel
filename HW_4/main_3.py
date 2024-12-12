from random import *

def get_random_list():
    return [randint(1,100) for i in range(randint(3, 10))]


def my_function(my_list):
    print(my_list, end=" == ")

    new_list = [my_list[0], my_list[2], my_list[-2]]

    print(new_list)

my_function([1, 2, 3, 4, 5, 6, 7, 9])    # Приклад з завдання
my_function([1, 1, 2, 1])                # Приклад з завдання
my_function([6, 3, 7])                   # Приклад з завдання

print()

my_function(get_random_list())
