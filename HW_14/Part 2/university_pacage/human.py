"""
Модуль, що містить клас Human, який представляє загальну концепцію людини.
"""

class Human:
    """
    Клас, що представляє людину.

    Атрибути:
        gender (str): Стать людини ("Male", "Female" або інше).
        age (int): Вік людини (у роках).
        first_name (str): Ім'я людини.
        last_name (str): Прізвище людини.
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """
        Ініціалізує об'єкт класу Human.

        Параметри:
            gender (str): Стать людини.
            age (int): Вік людини.
            first_name (str): Ім'я людини.
            last_name (str): Прізвище людини.
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Повертає строкове представлення об'єкта Human.

        Повернення:
            str: Строка, що описує людину, включаючи ПІБ, стать та вік.
        """
        return f"Human: {self.first_name} {self.last_name}, стать: {self.gender}, {self.age} років"