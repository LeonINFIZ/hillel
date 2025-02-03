class Fraction:
    """
    Клас, що представляє звичайний дріб.
    Реалізує основні операції з дробами, такі як додавання, віднімання, множення та порівняння.
    """

    def __init__(self, a: int, b: int) -> None:
        """
        Ініціалізує новий об'єкт дробу.

        :param a: Чисельник дробу.
        :param b: Знаменник дробу.
        :raises ValueError: Якщо знаменник дорівнює нулю.
        """
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.a = a
        self.b = b
        self.value = self.a / self.b

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Перевизначає оператор множення (*) для множення двох дробів.

        :param other: Інший дріб для множення.
        :type other: Fraction
        :return: Новий об'єкт дробу, що є результатом множення.
        :rtype: Fraction
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Перевизначає оператор додавання (+) для додавання двох дробів.

        :param other: Інший дріб для додавання.
        :type other: Fraction
        :return: Новий об'єкт дробу, що є результатом додавання.
        :rtype: Fraction
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Перевизначає оператор віднімання (-) для віднімання двох дробів.

        :param other: Інший дріб для віднімання.
        :type other: Fraction
        :return: Новий об'єкт дробу, що є результатом віднімання.
        :rtype: Fraction
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Перевизначає оператор рівності (==) для порівняння двох дробів на рівність.
        Порівняння відбувається за значенням дробу.

        :param other: Інший дріб для порівняння.
        :type other: Fraction
        :return: True, якщо дроби рівні, False в іншому випадку.
        :rtype: bool
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        return self.value == other.value

    def __gt__(self, other: 'Fraction') -> bool:
        """
        Перевизначає оператор "більше" (>) для порівняння двох дробів.
        Порівняння відбувається за значенням дробу.

        :param other: Інший дріб для порівняння.
        :type other: Fraction
        :return: True, якщо перший дріб більший за другий, False в іншому випадку.
        :rtype: bool
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        return self.value > other.value

    def __lt__(self, other: 'Fraction') -> bool:
        """
        Перевизначає оператор "менше" (<) для порівняння двох дробів.
        Порівняння відбувається за значенням дробу.

        :param other: Інший дріб для порівняння.
        :type other: Fraction
        :return: True, якщо перший дріб менший за другий, False в іншому випадку.
        :rtype: bool
        :raises TypeError: Якщо other не є екземпляром класу Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Операнд справа повинен бути екземпляром класу Fraction")
        return self.value < other.value

    def __str__(self) -> str:
        """
        Перевизначає метод str() для рядкового представлення об'єкта Fraction.
        Повертає рядок у форматі "Fraction: чисельник, знаменник".

        :return: Рядкове представлення дробу.
        :rtype: str
        """
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
print(f_c)
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
print(f_d)
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
print(f_e)
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
