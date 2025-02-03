class Rectangle:
    """
    Клас, що представляє прямокутник із заданою шириною та висотою.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Ініціалізує новий об'єкт прямокутника.

        :param width: Ширина прямокутника.
        :param height: Висота прямокутника.
        :raises TypeError: Якщо ширина або висота не є числами.
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина повинна бути числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Висота повинна бути числом")
        self.width = width
        self.height = height

    def get_square(self) -> float:
        """
        Обчислює та повертає площу прямокутника.

        :return: Площа прямокутника.
        :rtype: float
        """
        return self.width * self.height

    def __eq__(self, other: 'Rectangle') -> bool:
        """
        Перевизначає оператор рівності (==) для порівняння двох прямокутників за площею.

        :param other: Інший прямокутник для порівняння.
        :type other: Rectangle
        :return: True, якщо площі прямокутників рівні, False в іншому випадку.
        :rtype: bool
        :raises TypeError: Якщо other не є екземпляром класу Rectangle.
        """
        if not isinstance(other, Rectangle):
            raise TypeError("Операнд справа повинен бути екземпляром класу Rectangle")
        return self.get_square() == other.get_square()

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        """
        Перевизначає оператор додавання (+) для "додавання" двох прямокутників.
        Площа нового прямокутника буде дорівнювати сумі площ вихідних прямокутників.
        Ширина нового прямокутника береться від першого прямокутника, а висота розраховується виходячи із загальної площі.

        :param other: Інший прямокутник для додавання.
        :type other: Rectangle
        :return: Новий прямокутник, площа якого дорівнює сумі площ вихідних прямокутників.
        :rtype: Rectangle
        :raises TypeError: Якщо other не є екземпляром класу Rectangle.
        """
        if not isinstance(other, Rectangle):
            raise TypeError("Операнд справа повинен бути екземпляром класу Rectangle")
        new_height = (self.get_square() + other.get_square()) / self.width
        return Rectangle(self.width, new_height)

    def __mul__(self, n: int) -> 'Rectangle':
        """
        Перевизначає оператор множення (*) для "множення" прямокутника на число.
        Площа нового прямокутника буде збільшена в n разів.
        Ширина нового прямокутника береться від вихідного прямокутника, а висота розраховується виходячи з нової площі.

        :param n: Число, на яке потрібно "помножити" прямокутник.
        :type n: int
        :return: Новий прямокутник, площа якого в n разів більша за площу вихідного прямокутника.
        :rtype: Rectangle
        :raises TypeError: Якщо n не є цілим числом.
        """
        if not isinstance(n, int):
            raise TypeError("Множник повинен бути цілим числом")
        new_height = (self.get_square() * n) / self.width
        return Rectangle(self.width, new_height)

    def __str__(self) -> str:
        """
        Перевизначає метод str() для рядкового представлення об'єкта Rectangle.

        :return: Рядкове представлення прямокутника у форматі "Rectangle: (W = ширина, H = висота, S = площа)".
        :rtype: str
        """
        return f"Rectangle: (W = {self.width}, H = {self.height}, S = {self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
print(r1)
print(r2)

r3 = r1 + r2
assert r3.get_square() == r1.get_square() + r2.get_square(), 'Test3'
print(r3)

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4)

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print(Rectangle(3, 6) == Rectangle(2, 9))
