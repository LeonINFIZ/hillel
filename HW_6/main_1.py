import string

text = input("Enter the interval <letter>-<letter>: ")  # Наприклад: a-H

from_letter = text[0]
to_letter = text[-1]

# Рядок з усіма буквами
all_letters = string.ascii_letters

# Отримуємо індекси початкової та кінцевої літери
from_num = all_letters.index(from_letter)
to_num = all_letters.index(to_letter)

if from_num <= to_num:
    output_text = all_letters[from_num:to_num + 1]
else:
    output_text = all_letters[to_num:from_num + 1]
    output_text = output_text[::-1]

print(f"Your INTERVAL is:\t{from_letter}-{to_letter}")
print(f"Your TEXT is:\t\t{output_text}")
