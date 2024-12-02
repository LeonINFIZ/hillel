num = int(input("Введіть 4-х значне число: ")) # або num = 0, для того щоб ініціалізувати змінну

while (num < 1000 or num > 9999):
    num = int(input("Введіть 4-х значне число: "))

print(num // 1000) # 1
print(num % 10 ** 3 // 10 ** 2) # 2
print(num % 10 ** 2 // 10) # 3
print(num % 10) # 4

