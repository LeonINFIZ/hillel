go_next = "y"

while go_next == "y":
    while True:
        try:
            num1 = int(input("Перше число = "))
            break  # Если преобразование прошло успешно, выходим из цикла
        except ValueError:
            print("Помилка. Потрібно ввести число.")  # Сообщение об ошибке

    while True:
        try:
            num2 = int(input("Друге число = "))
            break  # Если преобразование прошло успешно, выходим из цикла
        except ValueError:
            print("Помилка. Потрібно ввести число.")  # Сообщение об ошибке


    print("\nВкажіть операцію:\n1. Додавання\t(+)\n2. Віднімання\t(-)\n3. Множення\t\t(*)\n4. Ділення\t\t(/)\n")
    answer = int(input("Відповідь: "))

    while (answer < 1 or answer > 4):
        print("Помилка. Вкажіть значення від 1 до 4")
        answer = int(input("Відповідь: "))

    print()

    if answer == 1:
        result = num1 + num2
        print(f"{num1} + {num2} =", result)

    elif answer == 2:
        result = num1 - num2
        print(f"{num1} - {num2} =", result)

    elif answer == 3:
        result = num1 * num2
        print(f"{num1} * {num2} =", result)

    elif answer == 4:
        result = num1 / num2
        print(f"{num1} / {num2} =", round(result, 5))

    go_next = input("\nСпробувати ще раз? (y) / Інший текст - щоб завершити роботу: ")
    print()

else:
    print("Допобачення!")



