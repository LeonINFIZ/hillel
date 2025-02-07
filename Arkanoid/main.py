import random
import pygame
import json
import time
import matplotlib.pyplot as plt
from config import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Ball")


def speed_up():
    global BALL_SPEED, PADDLE_SPEED
    BALL_SPEED += (BALL_SPEED * SPEED_UP) / 100
    PADDLE_SPEED += (PADDLE_SPEED * SPEED_UP) / 100

def reset_speed():
    global BALL_SPEED, PADDLE_SPEED
    BALL_SPEED = DEFAULT_BALL_SPEED
    PADDLE_SPEED = DEFAULT_PADDLE_SPEED

def draw_message(text: str, color: str, y_offset: int = 0):
    font = pygame.font.Font(None, 50)
    message = font.render(text, True, color)
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(message, rect)


def reset_game(game_status: str = "LOSE"):
    global ball, paddle, bricks, win, lose, BALL_SPEED, PADDLE_SPEED, LEVEL, start_time, bricks_broken
    ball = Ball()
    paddle = Paddle()
    bricks = [Brick(x, y) for x in range(50, WIDTH - 50, 80) for y in range(50, 200, 30)]
    win = False
    lose = False
    start_time = time.time()
    bricks_broken = 0

    if game_status == "WIN":
        speed_up()
        LEVEL += 1
    elif game_status == "LOSE":
        reset_speed()
        LEVEL = 1

    pygame.display.set_caption(f"Arkanoid Ball | LEVEL {LEVEL}")


def save_statistics():
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    stats = {"time": elapsed_time, "bricks_broken": bricks_broken}
    try:
        with open("statistics.json", "r", encoding="utf-8") as statistics_file:
            data = json.load(statistics_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(stats)
    with open("statistics.json", "w", encoding="utf-8") as statistics_file:
        json.dump(data, statistics_file, indent=4)

    print("Statistics saved to statistics.json")


def plot_statistics():
    try:
        with open("statistics.json", "r", encoding="utf-8") as statistics_file:
            data = json.load(statistics_file)
        times = [entry["time"] for entry in data]
        bricks = [entry["bricks_broken"] for entry in data]
        plt.figure(figsize=(8, 6))
        plt.plot(times, bricks, marker="o", linestyle="-", color="red")
        plt.xlabel("Time (sec)")
        plt.ylabel("Bricks broken")
        plt.title("Game statistics")
        plt.grid()
        plt.show()
    except (FileNotFoundError, json.JSONDecodeError):
        print("Statistics file not found")


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 7.5, 485, 15, 15)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = -BALL_SPEED

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx = -self.dx

        if self.rect.top <= 0:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 50, 500, 100, 10)

    def move(self, direction):
        if direction == "LEFT" and self.rect.left > 0:
            self.rect.x -= PADDLE_SPEED

        if direction == "RIGHT" and self.rect.right < WIDTH:
            self.rect.x += PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 75, 20)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)


reset_game()

running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (win or lose):
                if event.key == pygame.K_r:
                    if win:
                        reset_game("WIN")
                    elif lose:
                        reset_game("LOSE")
                if event.key == pygame.K_s:
                    plot_statistics()

    if not win and not lose:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("LEFT")
        if keys[pygame.K_RIGHT]:
            paddle.move("RIGHT")

        ball.move()

        if ball.rect.colliderect(paddle.rect):
            ball.dy = -ball.dy

        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                bricks.remove(brick)
                bricks_broken += 1
                ball.dy = -ball.dy
                break

        if ball.rect.bottom >= HEIGHT:
            save_statistics()
            lose = True

        if not bricks:
            save_statistics()
            win = True

    ball.draw()
    paddle.draw()

    for brick in bricks:
        brick.draw()

    if win:
        draw_message("You Win!", GREEN)
        draw_message("Press 'r' for start game again", GREEN, 50)
    elif lose:
        draw_message("You Lose! Try again!", RED)
        draw_message("Press 'r' for start game again", RED, 50)

    pygame.display.flip()
    pygame.time.delay(7)

pygame.quit()
