import string

def text_to_hashtag(text):

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

text_to_hashtag("Python Community")
text_to_hashtag("i like python community!")
text_to_hashtag("Should, I. subscribe? Yes!")

print()

text_to_hashtag("Welcome to @Python_Community!")
text_to_hashtag("Good morning! #HaveAGreatDay :)")
text_to_hashtag("E-mail me at: example@example.com!")
text_to_hashtag("Follow us @Python & join the fun!")
text_to_hashtag("Hello #World! It's a @beautiful day.")
text_to_hashtag("50% off on all items!!! $$$")

print()

# Строка де є більше ніж 140 символів
text_to_hashtag("In today's world of rapid technological advancements, embracing change and staying adaptive are key to unlocking endless opportunities for growth, innovation, and long-term success!")
