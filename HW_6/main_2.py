from numpy.random import choice
import string

num_time = -1

while num_time < 0 or num_time > 8640000:
    try:
        num_time = int(input("Enter time in seconds = "))

        if 0 < num_time < 8640000:
            break
        else:
            print("\n[ERROR => Enter time from 0 to 8640000.]\n")
            continue
    except ValueError:
        print("\n[ERROR => Not a valid input. Try again.]\n")

days = num_time // (24 * 60 * 60)
hours = (num_time % (24 * 60 * 60)) // (60 * 60)
minutes = (num_time % (60 * 60)) // 60
seconds = num_time % 60

if 11 <= days % 100 <= 14:
    day_declension = "днів"
else:
    last_digit = days % 10
    if last_digit == 1:
        day_declension = "день"
    elif 2 <= last_digit <= 4:
        day_declension = "дні"
    else:
        day_declension = "днів"

print(days, " ", day_declension, ", ", str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2), sep="")
