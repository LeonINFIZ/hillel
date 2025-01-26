class Human:
    """
    Клас, що представляє людину.

    Атрибути:
        gender (str): Стать людини.
        age (int): Вік людини.
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
            str: Строка, що описує людину.
        """
        return f"Human: {self.first_name} {self.last_name}, gender: {self.gender}, {self.age} years old"


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
            str: Строка, що описує студента.
        """
        return f"Student [{self.record_book}]: {self.first_name} {self.last_name}, gender: {self.gender}, {self.age} years old"


class Group:
    """
    Клас, що представляє групу студентів.

    Атрибути:
        number (str): Номер групи.
        group (set): Множина студентів у групі.
    """

    def __init__(self, number: str) -> None:
        """
        Ініціалізує об'єкт класу Group.

        Параметри:
            number (str): Номер групи.
        """
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """
        Додає студента до групи.

        Параметри:
            student (Student): Об'єкт студента.
        """
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        """
        Видаляє студента з групи за його прізвищем.

        Параметри:
            last_name (str): Прізвище студента.
        """
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str) -> Student | None:
        """
        Шукає студента в групі за його прізвищем.

        Параметри:
            last_name (str): Прізвище студента.

        Повернення:
            Student | None: Знайдений студент або None, якщо такого немає.
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """
        Повертає строкове представлення об'єкта Group.

        Повернення:
            str: Строка, що описує групу та її студентів.
        """

        all_students = "\n".join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr, "\n")

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
