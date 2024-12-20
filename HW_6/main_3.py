while True:
    try:
        num = int(input("Enter a number = "))
        break
    except ValueError:
        print("\n[ERROR => Not a valid input. Try again.]\n")

while num > 9:
    multiplication_of_numbers = 1

    for digit in str(num):
        multiplication_of_numbers *= int(digit)

    num = multiplication_of_numbers

print(num)
