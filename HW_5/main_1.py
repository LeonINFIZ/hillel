import keyword
import string

punctuation = set(string.punctuation)

print(punctuation)
punctuation.remove('_')

print(keyword.kwlist)

text = input("\nВведіть ім'я змінної: ")

if text in keyword.kwlist or text.find(" ") != -1 or text[0].isdigit():
    print("False")
else:
    for i in range(len(text)):
        if text[i] in punctuation or text[i].isupper() or (text[i] == "_" and text[i+1] == "_"):
            print("False")
            break
    else:
        print("True")