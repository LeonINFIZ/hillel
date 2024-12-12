def my_function(my_list):
    print(my_list, end=" => ")

    if not my_list:
        print(0)
    else:
        summ = 0

        for i, num in enumerate(my_list):
            if i % 2 == 0:
                summ += num

        print(summ*my_list[-1])

my_function([0, 1, 7, 2, 4, 8])
my_function([1, 3, 5])
my_function([6])
my_function([])


