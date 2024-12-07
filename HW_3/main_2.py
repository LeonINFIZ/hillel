#########################

my_list = [12, 3, 4, 10]

print(my_list, end='')

pop_num = my_list.pop()
my_list.insert(0, pop_num)

print(" =>", my_list)

#########################

my_list = [1]

print(my_list, end='')

pop_num = my_list.pop()
my_list.insert(0, pop_num)

print(" =>", my_list)

#########################

my_list = []

print(my_list, end='')

if my_list:
    pop_num = my_list.pop()
    my_list.insert(0, pop_num)

    print(" =>", my_list)
else:
    print(" => []")

#########################

my_list = [12, 3, 4, 10, 8]

print(my_list, end='')

pop_num = my_list.pop()
my_list.insert(0, pop_num)

print(" =>", my_list)

#########################
