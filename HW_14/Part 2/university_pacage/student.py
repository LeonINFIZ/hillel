"""
Модуль, що містить клас Student, який представляє студента та успадковується від класу Human.
"""

from .human import Human  # Імпортуємо Human з модуля human.py

class Student(Human):
    """
    Клас, що представляє студента, успадковує клас Human.

    Додатковий атрибут:
        record_book (str): Номер залікової книжки студента.
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """
        Ініціалізує об'єкт класу Student.

        Параметри:
            gender (str): Стать студента.
            age (int): Вік студента.
            first_name (str): Ім'я студента.
            last_name (str): Прізвище студента.
            record_book (str): Номер залікової книжки.
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Повертає строкове представлення об'єкта Student.

        Повернення:
            str: Строка, що описує студента, включаючи номер залікової книжки, ПІБ, стать та вік.
        """
        return f"Student [{self.record_book}]: {self.first_name} {self.last_name}, стать: {self.gender}, {self.age} років"

    def __eq__(self, other):
        """
        Реалізує порівняння об'єктів Student на основі їх строкового представлення.

        Параметри:
            other: Інший об'єкт для порівняння.

        Повернення:
            bool: True, якщо строкові представлення об'єктів однакові, False - інакше.
        """
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        """
        Реалізує хешування об'єктів Student на основі їх строкового представлення.

        Це необхідно для того, щоб об'єкти Student можна було використовувати в множинах (set) та словниках (dict) як ключі.
        Хешування базується на рядковому представленні об'єкта, щоб бути узгодженим з методом __eq__.

        Повернення:
            int: Хеш-значення об'єкта Student.
        """
        return hash(str(self))