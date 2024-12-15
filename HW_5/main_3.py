import string

text = input("Введіть текст який треба змінити до типу hashtag: ")

print(f"\'{text}\' -> ", end="")

punctuation = set(string.punctuation) # Розділяємо символи на об'єкти списку

hashtag = ""

# Видаляємо всі символи, які є у тексті
for symbol in text:
    if symbol not in punctuation:
        hashtag += symbol

# Розділяєемо новий текст за пробілами
split_text = hashtag.split()

# Замінюємо першу букву в на велику та дописуємо решту символів об'єкту з вже заданим хештегом
hashtag = "#"
for word in split_text:
    hashtag += word.title()

# Обрізаємо зайву частину тексту, не більше 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)

