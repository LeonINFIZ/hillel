def my_func(my_list):

    print(my_list, end='')

    middle_value = int(len(my_list) / 2)

    if len(my_list) % 2 != 0:
        first_list = my_list[:middle_value + 1]
        second_list = my_list[middle_value + 1:]
    else:
        first_list = my_list[:middle_value]
        second_list = my_list[middle_value:]

    result_list = [first_list, second_list]

    print(" =>", result_list)


my_func([1, 2, 3, 4, 5, 6])
my_func([1, 2, 3])
my_func([1, 2, 3, 4, 5])
my_func([1])
my_func([])

