def common_elements():
    """
    Finds common elements between two lists generated based on given conditions.

    List 1: Numbers from 1 to 100 that are divisible by 3 without a remainder.
    List 2: Numbers from 1 to 100 that are divisible by 5 without a remainder.

    Returns:
        set: A set of common elements between the two lists.
    """

    # Генеруємо список з чисел, кратних 3
    list1 = [x for x in range(1, 101) if x % 3 == 0]
    # Генеруємо список з чисел, кратних 5
    list2 = [x for x in range(1, 101) if x % 5 == 0]

    # Виводимо списки для наочності
    print(list1)
    print(list2)

    # Повертаємо множину спільних елементів
    return set(list1).intersection(list2)


# Перевірка роботи функції
print("Спільні елементи:", common_elements())
