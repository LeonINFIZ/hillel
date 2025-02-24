import turtle

# Настройка экрана
screen = turtle.Screen()
screen.setup(800, 600)  # Размер окна 800x600
screen.bgcolor("black")  # Черный фон
screen.tracer(0)  # Отключение автоматического обновления для ручного контроля

# Создание платформы
paddle = turtle.Turtle()
paddle.shape("square")  # Форма — прямоугольник
paddle.color("blue")  # Цвет синий
paddle.shapesize(stretch_wid=1, stretch_len=5)  # Размер: 1 в высоту, 5 в ширину
paddle.penup()  # Отключение рисования линии
paddle.goto(0, -250)  # Начальная позиция внизу экрана

# Создание мяча
ball = turtle.Turtle()
ball.shape("circle")  # Форма — круг
ball.color("red")  # Цвет красный
ball.penup()
ball.goto(0, 0)  # Начальная позиция в центре
ball.dx = 3  # Скорость по оси X
ball.dy = -3  # Скорость по оси Y (вниз)

# Создание кирпичей
bricks = []
for i in range(5):  # 5 рядов
    for j in range(10):  # 10 кирпичей в ряду
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("green")  # Цвет зеленый
        brick.shapesize(stretch_wid=1, stretch_len=3)  # Размер: 1x3
        brick.penup()
        x = -350 + j * 70  # Позиция по X
        y = 250 - i * 20  # Позиция по Y
        brick.goto(x, y)
        bricks.append(brick)

# Настройка очков
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()  # Скрытие черепахи
score_turtle.penup()
score_turtle.goto(-380, 260)  # Позиция вверху слева
score_turtle.color("white")
score_turtle.write("Score: 0", font=("Arial", 16, "normal"))

# Надпись для сообщений
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 0)  # Центр экрана
message_turtle.color("white")

# Флаги для управления
left_pressed = False
right_pressed = False
game_running = True

# Функции управления платформой
def left_press():
    global left_pressed
    left_pressed = True

def left_release():
    global left_pressed
    left_pressed = False

def right_press():
    global right_pressed
    right_pressed = True

def right_release():
    global right_pressed
    right_pressed = False

# Привязка клавиш
screen.listen()
screen.onkeypress(left_press, "Left")
screen.onkeyrelease(left_release, "Left")
screen.onkeypress(right_press, "Right")
screen.onkeyrelease(right_release, "Right")

# Основной игровой цикл
def move_ball():
    global game_running, score
    if game_running:
        # Движение платформы
        if left_pressed:
            x = paddle.xcor()
            if x > -350:  # Проверка левой границы
                paddle.setx(x - 5)
        if right_pressed:
            x = paddle.xcor()
            if x < 350:  # Проверка правой границы
                paddle.setx(x + 5)

        # Движение мяча
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Проверка столкновений со стенами
        if ball.xcor() > 390 or ball.xcor() < -390:  # Боковые стены
            ball.dx *= -1
        if ball.ycor() > 290:  # Верхняя стена
            ball.dy *= -1

        # Проверка столкновения с платформой
        if ball.ycor() < -240 and ball.distance(paddle) < 50:
            ball.dy *= -1

        # Проверка столкновения с кирпичами
        for brick in bricks[:]:  # Копия списка для безопасного удаления
            if ball.distance(brick) < 20:
                brick.hideturtle()  # Скрытие кирпича
                bricks.remove(brick)  # Удаление из списка
                ball.dy *= -1  # Отскок мяча
                score += 1  # Увеличение очков
                score_turtle.clear()
                score_turtle.write(f"Score: {score}", font=("Arial", 16, "normal"))

        # Проверка падения мяча ниже платформы
        if ball.ycor() < -290:
            game_running = False
            message_turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))

        # Проверка победы
        if not bricks:
            game_running = False
            message_turtle.write("You Win!", align="center", font=("Arial", 24, "normal"))

        # Обновление экрана
        screen.update()
        screen.ontimer(move_ball, 20)  # Следующий вызов через 20 мс

# Запуск игры
move_ball()
turtle.mainloop()  # Запуск главного цикла