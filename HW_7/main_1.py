def say_hi(name, age):
    """
    Повертає привітання з іменем та віком.

    Параметри:
    name (str): Ім'я людини.
    age (int): Вік людини.

    Повертає:
    str: Привітання з ім’ям та віком.
    """
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
