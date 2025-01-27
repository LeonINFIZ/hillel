"""
Модуль, що містить класи для представлення навчальної групи та виняток для переповнення групи.
"""

from .student import Student

class FullGroup(Exception):
    """
    Виняток, що сигналізує про переповнення групи.
    """
    pass


class Group:
    """
    Клас, що представляє групу студентів.

    Атрибути:
        number (str): Номер групи.
        group (set[Student]): Множина студентів у групі.
        count_of_students (int): Кількість студентів у групі.
        group_capacity (int): Максимальна кількість студентів у групі.
    """

    def __init__(self, number: str, group_capacity: int = 10) -> None:
        """
        Ініціалізує об'єкт класу Group.

        Параметри:
            number (str): Номер групи.
            group_capacity (int): Максимальна кількість студентів у групі (за замовчуванням 10).
        """
        self.number = number
        self.group: set[Student] = set()
        self.count_of_students = 0
        self.group_capacity = group_capacity

    def add_student(self, student: Student) -> None:
        """
        Додає студента до групи.

        Параметри:
            student (Student): Об'єкт студента класу Student.

        Піднімає:
            FullGroup: Якщо група вже переповнена і неможливо додати нового студента.
        """
        if self.count_of_students < self.group_capacity:
            self.count_of_students += 1
            self.group.add(student)
        else:
            raise FullGroup(f"Група {self.number} переповнена. Неможливо додати студента.")

    def delete_student(self, last_name: str) -> None:
        """
        Видаляє студента з групи за його прізвищем.

        Параметри:
            last_name (str): Прізвище студента.

        Примітка:
            Якщо студент із вказаним прізвищем не знайдений у групі, метод не викликає помилок.
        """
        try:
            self.group.remove(self.find_student(last_name))
        except KeyError:
            pass
        else:
            self.count_of_students -= 1

    def find_student(self, last_name: str) -> Student | None:
        """
        Шукає студента в групі за його прізвищем.

        Параметри:
            last_name (str): Прізвище студента.

        Повернення:
            Student | None: Знайдений студент (об'єкт класу Student) або None, якщо студент не знайдений.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """
        Повертає строкове представлення об'єкта Group.

        Повернення:
            str: Строка, що описує групу (номер групи) та список студентів у групі.
        """
        all_students = "\n".join(
            f"[{num + 1}/{self.count_of_students}] {str(student)}"
            for num, student in enumerate(self.group)
        )
        return f'Група: {self.number}\n{all_students}'