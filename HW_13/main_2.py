class Counter:
    """
    Клас, що представляє лічильник зі змінним поточним значенням, мінімумом і максимумом.

    Атрибути:
        current (int): Поточне значення лічильника.
        min_value (int): Мінімально допустиме значення.
        max_value (int): Максимально допустиме значення.
    """

    def __init__(self, current: int = 0, min_value: int = 0, max_value: int = 10) -> None:
        """
        Ініціалізує об'єкт класу Counter.

        Параметри:
            current (int): Початкове значення лічильника. За замовчуванням 0.
            min_value (int): Мінімально допустиме значення. За замовчуванням 0.
            max_value (int): Максимально допустиме значення. За замовчуванням 10.
        """
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        """
        Встановлює поточне значення лічильника.

        Параметри:
            start (int): Нове значення лічильника.
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """
        Встановлює максимальне значення лічильника.

        Параметри:
            max_max (int): Нове максимальне значення.
        """
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """
        Встановлює мінімальне значення лічильника.

        Параметри:
            min_min (int): Нове мінімальне значення.
        """
        self.min_value = min_min

    def step_up(self) -> None:
        """
        Збільшує поточне значення лічильника на 1.
        Якщо досягнуто максимального значення, викликає помилку.
        """
        try:
            if self.current < self.max_value:
                self.current += 1
            else:
                raise ValueError("Досягнуто максимуму")
        except ValueError as err:
            print(f"Помилка: {err}")

    def step_down(self) -> None:
        """
        Зменшує поточне значення лічильника на 1.
        Якщо досягнуто мінімального значення, викликає помилку.
        """
        try:
            if self.current > self.min_value:
                self.current -= 1
            else:
                raise ValueError("Досягнуто мінімуму")
        except ValueError as err:
            print(f"Помилка: {err}")

    def get_current(self) -> int:
        """
        Повертає поточне значення лічильника.

        Повернення:
            int: Поточне значення лічильника.
        """
        return self.current

    def __str__(self) -> str:
        """
        Повертає строкове представлення об'єкта Counter.

        Повернення:
            str: Строка, що описує поточне, мінімальне та максимальне значення лічильника.
        """
        return f"Counter: Value = {self.current}, MIN = {self.min_value}, MAX = {self.max_value}"


counter = Counter()

print(counter)  # Counter: Value = 0, MIN = 0, MAX = 10

counter.set_current(7)
counter.step_up()  # 8
counter.step_up()  # 9
counter.step_up()  # 10

print(counter)  # Counter: Value = 10, MIN = 0, MAX = 10

assert counter.get_current() == 10, 'Test1'

print("-------")
counter.step_up()  # [ValueError] Помилка: Досягнуто максимуму
print("-------")

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()  # 9
counter.step_down()  # 8
counter.step_down()  # 7

print(counter)  # Counter: Value = 7, MIN = 7, MAX = 10

assert counter.get_current() == 7, 'Test3'

print("******")
counter.step_down()  # [ValueError] Помилка: Досягнуто мінімуму
print("******")

assert counter.get_current() == 7, 'Test4'
