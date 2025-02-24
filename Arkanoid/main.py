import random
import pygame
import json
import time
import matplotlib.pyplot as plt
from config import *
from collections import defaultdict
import numpy as np
from scipy.interpolate import make_interp_spline

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Ball")
pygame.display.set_icon(pygame.image.load('src/title_icon.png'))

sound_loss = pygame.mixer.Sound("src/sound/Loss.ogg")
sound_broke_a_brick = pygame.mixer.Sound("src/sound/Broke a brick.ogg")
sound_start = pygame.mixer.Sound("src/sound/Start.ogg")
sound_knock_on_the_platform = pygame.mixer.Sound("src/sound/Knock on the platform.ogg")
sound_knock_on_the_wall = pygame.mixer.Sound("src/sound/Knock on the wall.ogg")
sounds = (sound_loss, sound_start, sound_broke_a_brick, sound_knock_on_the_wall, sound_knock_on_the_platform)
def set_volume_to_sounds(volume, sound):
    sound.set_volume(volume)

for sound in sounds:
    set_volume_to_sounds(1, sound)


def speed_up():
    global BALL_SPEED, PADDLE_SPEED
    BALL_SPEED += (BALL_SPEED * SPEED_UP) / 100
    PADDLE_SPEED += (PADDLE_SPEED * SPEED_UP) / 100


def reset_speed():
    global BALL_SPEED, PADDLE_SPEED
    BALL_SPEED = DEFAULT_BALL_SPEED
    PADDLE_SPEED = DEFAULT_PADDLE_SPEED


def draw_message(text: str, color: str, x_offset: int = 0, y_offset: int = 0, font_size: int = 50,
                 align: str = "center"):
    font = pygame.font.Font(None, font_size)
    message = font.render(text, True, color)
    if align == "center":
        rect = message.get_rect(center=(WIDTH // 2 + x_offset, HEIGHT // 2 + y_offset))
    elif align == "right":
        rect = message.get_rect(midright=(WIDTH // 2 + x_offset, HEIGHT // 2 + y_offset))
    elif align == "left":
        rect = message.get_rect(midleft=(WIDTH // 2 + x_offset, HEIGHT // 2 + y_offset))

    screen.blit(message, rect)


class GameTime:
    """
    Клас для вимірювання ігрового часу з функцією паузи (stop) та скидання (reset).
    """
    __start_time: float = 0.0  # Час останнього запуску таймера
    __paused_duration: float = 0.0 # Накопичений час пауз

    @classmethod
    def start(cls):
        """
        Запускає або відновлює таймер.
        Якщо таймер був на паузі, відновлює відлік з моменту паузи.
        Викликається як GameTime.start().
        """
        if cls.__start_time == 0.0:  # Якщо таймер не був запущений або був скинутий
            cls.__start_time = time.time()  # Запам'ятовуємо час початку
        else:
            # Якщо таймер був на паузі (start() викликається після stop())
            # Відновлюємо відлік, коригуючи час початку, щоб врахувати паузу
            pause_offset = time.time() - (cls.__start_time + cls.__paused_duration)
            cls.__start_time += pause_offset  # Коригуємо час початку
            cls.__paused_duration = 0.0  # Скидаємо накопичений час пауз, бо пауза закінчилась


    @classmethod
    def stop(cls):
        """
        Призупиняє таймер (пауза).
        Запам'ятовує пройдений час з моменту останнього start().
        При наступному start() відлік часу буде відновлено з цього моменту.
        Повертає пройдений час з моменту останнього start().
        Викликається як GameTime.stop().
        """
        if cls.__start_time == 0.0: # Перевірка, чи був запущений таймер
            return 0.0 # Якщо таймер не був запущений, повертаємо 0

        elapsed_time = time.time() - cls.__start_time # Обчислюємо пройдений час
        rounded_time = round(elapsed_time, 2) # Округляємо до 2 знаків після коми

        cls.__paused_duration += rounded_time # **Накопичуємо час паузи**
        cls.__start_time = 0.0 # **Скидаємо час початку, але не накопичений час пауз**

        return rounded_time

    @classmethod
    def get_game_time(cls):
        """
        Повертає поточний ігровий час, враховуючи паузи.
        Викликається як GameTime.get_game_time().
        """
        if cls.__start_time == 0.0: # Таймер не запущений або на паузі
            return round(cls.__paused_duration, 2) # Повертаємо накопичений час пауз
        else:
            elapsed_time = time.time() - cls.__start_time # Обчислюємо час від останнього start()
            return round(elapsed_time + cls.__paused_duration, 2) # Додаємо накопичений час пауз


    @classmethod
    def reset(cls):
        """
        Повністю скидає таймер, включаючи накопичений час пауз.
        Після виклику reset(), потрібно знову викликати start(), щоб почати відлік часу з нуля.
        Викликається як GameTime.reset().
        """
        cls.__start_time = 0.0
        cls.__paused_duration = 0.0



def reset_game(game_status: str = "LOSE"):
    global ball, paddle, bricks, win, lose, BALL_SPEED, PADDLE_SPEED, LEVEL, bricks_broken
    ball = Ball()
    paddle = Paddle()
    bricks = [Brick(x, y) for x in range(50, WIDTH - 50, 80) for y in range(50, 200, 30)]
    win = False
    lose = False
    bricks_broken = 0

    paddle.rect = pygame.Rect(WIDTH // 2 - 100, 500, 200, 10)

    if game_status == "WIN":
        speed_up()
        LEVEL += 1
    elif game_status == "LOSE":
        GameTime.reset()
        speed_up()
        speed_up()
        speed_up()
        reset_speed()
        LEVEL = 1



def save_statistics():
    stats = {"time": GameTime.get_game_time(), "bricks_broken": bricks_broken, "level": LEVEL}
    try:
        with open(STATISTICS_FILE_PATH, "r", encoding="utf-8") as stats_file:
            data = json.load(stats_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(stats)
    with open(STATISTICS_FILE_PATH, "w", encoding="utf-8") as stats_file:
        json.dump(data, stats_file, indent=4)

    print(
        f"Statistics saved to {STATISTICS_FILE_PATH}.\nGAME INFO: Time = {stats['time']} sec | {stats['bricks_broken']} bricks broken | {stats['level']} level\n")


def plot_statistics():
    try:
        with open(STATISTICS_FILE_PATH, "r", encoding="utf-8") as statistics_file:
            data = json.load(statistics_file)

        # Группируем данные по уровням, а затем по времени внутри каждого уровня
        data_by_level__time = defaultdict(lambda: defaultdict(list))
        max_bricks_broken = 0  # Для определения верхней границы полос уровней
        for entry in data:
            level = entry["level"]
            time = entry["time"]
            bricks_broken = entry["bricks_broken"]
            data_by_level__time[level][time].append(bricks_broken)
            max_bricks_broken = max(max_bricks_broken, bricks_broken)

        plt.figure(figsize=(12, 9))
        cmap = plt.colormaps.get_cmap('tab10')

        num_levels = len(data_by_level__time)
        level_band_height = (max_bricks_broken * 0.9) / num_levels  # Высота полосы уровня, 90% от макс. кол-ва кирпичей
        level_band_bottom = 0

        # Рисуем горизонтальные полосы уровней
        for i, level in enumerate(sorted(data_by_level__time.keys())):
            band_color = cmap(i)
            plt.axhspan(level_band_bottom, level_band_bottom + level_band_height, facecolor=band_color, alpha=0.2,
                        label=f'Уровень {level} полоса')  # label для легенды
            plt.text(0, level_band_bottom + level_band_height / 2, f'Уровень {level}', ha='left', va='center',
                     color='black', fontsize=9)  # Метка уровня
            level_band_bottom += level_band_height

        # Рисуем линии графиков поверх полос
        for i, level in enumerate(sorted(data_by_level__time.keys())):
            level__time_data = data_by_level__time[level]
            unique__times = sorted(level__time_data.keys())
            averaged_bricks = [np.mean(level__time_data[t]) for t in unique__times]

            times_np = np.array(unique__times)
            bricks_np = np.array(averaged_bricks)

            plt.plot(times_np, bricks_np, color=cmap(i), label=f"Уровень {level} линия", linewidth=2, marker='o',
                     markersize=5)  # label для легенды

        plt.xlabel("Время (сек)", fontsize=12)
        plt.ylabel("Разбито кирпичей", fontsize=12)
        plt.title("Статистика игры с горизонтальными полосами уровней", fontsize=14)
        plt.grid(True, axis='x', linestyle='--', alpha=0.7)  # Сетка только по X
        plt.legend(title="Уровень", fontsize=10, title_fontsize=11, loc='upper left')  # Легенда в верхнем левом углу
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.ylim(bottom=0, top=max_bricks_broken * 1.1)  # Y-ось немного выше максимума
        plt.tight_layout()
        plt.show()

    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Файл статистики ({STATISTICS_FILE_PATH}) не найден или имеет неверный формат JSON.")


class Paddle:

    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 100, 500, 200, 10)
        self.moving = False

    def move(self, direction):
        if direction == "LEFT":
            if self.rect.left > 0:
                self.rect.x -= PADDLE_SPEED
                self.moving = True
            else:
                self.moving = False

        if direction == "RIGHT":
            if self.rect.right < WIDTH:
                self.rect.x += PADDLE_SPEED
                self.moving = True
            else:
                self.moving = False

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect, border_radius=20)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 7.5, 485, 15, 15)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = -BALL_SPEED



    def move(self, start: bool=False, left: str=None, right: str=None, paddle: Paddle=None):

        if start:
            self.rect.x += self.dx
            self.rect.y += self.dy

            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.dx = -self.dx
                sound_knock_on_the_wall.play()

            if self.rect.top <= 0:
                self.dy = -self.dy
                sound_knock_on_the_wall.play()
        else:
            if left == "LEFT" and paddle.moving:
                self.rect.x -= PADDLE_SPEED
            else:
                self.rect.x += 0
            if right == "RIGHT" and paddle.moving:
                self.rect.x += PADDLE_SPEED
            else:
                self.rect.x += 0

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, self.rect)

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 75, 20)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect, border_radius=2)


reset_game()

running = True
start_playing = False

while running:

    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (win or lose):
                if event.key == pygame.K_r:
                    save_statistics()
                    start_playing = False
                    if win:
                        reset_game("WIN")
                    elif lose:
                        reset_game("LOSE")

                if event.key == pygame.K_s:
                    plot_statistics()

    if not win and not lose:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if start_playing:
                paddle.move("LEFT")
            else :
                paddle.move("LEFT")
                ball.move(start_playing, left="LEFT", paddle=paddle)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if start_playing:
                paddle.move("RIGHT")
            else:
                paddle.move("RIGHT")
                ball.move(start_playing, right="RIGHT", paddle=paddle)
        if keys[pygame.K_SPACE]:
            if not start_playing:
                start_playing = True
                sound_start.play()
                GameTime.start()

        ball.move(start_playing)

        if ball.rect.colliderect(paddle.rect):
            # Определяем относительную точку столкновения на платформе
            collision_point_x = ball.rect.right - paddle.rect.x
            normalized_collision_point = (collision_point_x / paddle.rect.width)

            # Отражаем вертикальную скорость
            ball.dy = -ball.dy
            if abs(ball.dy) < BALL_SPEED:  # Минимальная вертикальная скорость
                ball.dy = -BALL_SPEED * (-1 if ball.dy > 0 else 1)

            # Добавляем горизонтальное отклонение от точки удара
            #ball.dx += BALL_SPEED

            # Учитываем движение платформы
            if paddle.moving:  # Проверяем, двигалась ли платформа в момент удара
                if keys[pygame.K_LEFT]:  # Если двигалась влево
                    ball.dx -= BALL_SPEED / 2
                elif keys[pygame.K_RIGHT]:  # Если двигалась вправо
                    ball.dx += BALL_SPEED / 2

            # Ограничиваем горизонтальную скорость, чтобы не улетал слишком сильно
            ball.dx = max(-BALL_SPEED * 2, min(BALL_SPEED * 2, ball.dx))r

            sound_knock_on_the_platform.play()

        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                bricks.remove(brick)
                bricks_broken += 1
                ball.dy = -ball.dy
                sound_broke_a_brick.play()
                break

        if ball.rect.bottom >= HEIGHT:
            sound_loss.play()
            GameTime.stop()
            lose = True

        if not bricks:
            GameTime.stop()
            win = True

    ball.draw()
    paddle.draw()

    for brick in bricks:
        brick.draw()

    if win:
        draw_message("You Win!", GREEN, y_offset=-30)
        draw_message("Press 'r' for start game again", GREEN, y_offset=20)
    elif lose:
        draw_message("You Lose! Try again!", RED)
        draw_message("Press 'r' for start game again", RED, y_offset=50)

    if not lose or win:
        if not start_playing:
            draw_message("Press 'SPACE' for start", GREEN, y_offset=HEIGHT // 2 - 50, font_size=40)


        draw_message(f"TIME {GameTime.get_game_time()}", BLUE, x_offset=WIDTH // 2 - 130,
                     y_offset=HEIGHT // 2 - 50, font_size=30, align="left")

    else:
        draw_message(f"TIME {GameTime.get_game_time()}", BLUE, x_offset=WIDTH // 2 - 130,
                     y_offset=HEIGHT // 2 - 50, font_size=30, align="left")

    draw_message(f"LEVEL {LEVEL}", BLUE, x_offset=-WIDTH // 2 + 80, y_offset=HEIGHT // 2 - 50, font_size=30)

    pygame.display.flip()
    pygame.time.delay(7)

pygame.quit()
