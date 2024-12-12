def my_function(my_list):
    print(my_list, end=" -> ")
    zeros = []
    non_zeros = []

    for num in my_list:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)

    my_list = non_zeros + zeros
    print(my_list)


my_function([0, 1, 0, 12, 3])
my_function([0])
my_function([1, 0, 13, 0, 0, 0, 5])
my_function([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0])