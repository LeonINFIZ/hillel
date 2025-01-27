class FullGroup(Exception):
    """
    Виняток, що сигналізує про переповнення групи.
    """
    pass


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
        group (set[Student]): Множина студентів у групі.
        count_of_students (int): Кількість студентів у групі.
        group_capacity (int): Максимальна кількість студентів у групі.
    """

    def __init__(self, number: str, group_capacity: int = 10) -> None:
        self.number = number
        self.group: set[Student] = set()
        self.count_of_students = 0
        self.group_capacity = group_capacity

    def add_student(self, student: Student) -> None:
        """
        Додає студента до групи.

        Параметри:
            student (Student): Об'єкт студента.

        Піднімає:
            FullGroup: Якщо група вже переповнена.
        """
        if self.count_of_students < self.group_capacity:
            self.count_of_students += 1
            self.group.add(student)
        else:
            raise FullGroup(f"{self.number} is full")

    def delete_student(self, last_name: str) -> None:
        """
        Видаляє студента з групи за його прізвищем.

        Параметри:
            last_name (str): Прізвище студента.

        Якщо студент із вказаним прізвищем не знайдений, метод не викликає помилок.
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
        all_students = "\n".join(
            f"[{num + 1}/{self.count_of_students}] {str(student)}"
            for num, student in enumerate(self.group)
        )
        return f'Group: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'John', 'Doe', 'AN146')
st4 = Student('Female', 22, 'Anna', 'Smith', 'AN147')
st5 = Student('Male', 35, 'Mark', 'Twain', 'AN148')
st6 = Student('Female', 27, 'Sophia', 'Brown', 'AN149')
st7 = Student('Male', 32, 'David', 'Johnson', 'AN150')
st8 = Student('Female', 24, 'Emma', 'Davis', 'AN151')
st9 = Student('Male', 29, 'James', 'Wilson', 'AN152')
st10 = Student('Female', 26, 'Olivia', 'Taylor', 'AN153')
st11 = Student('Male', 31, 'Michael', 'Scott', 'AN154')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)  # [Error] PD1 is full
except FullGroup as error:
    print(f"[Error] {error}")

print(f"\n{gr}\n")

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
gr.delete_student('Doe')
gr.delete_student('Johnson')
print(gr)  # 7 students

gr.delete_student('Taylor')  # No error!
