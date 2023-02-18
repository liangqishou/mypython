import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏界面尺寸
WIDTH = 400
HEIGHT = 400

# 设置游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 定义贪吃蛇的初始位置和方向
snake = [(200, 200), (210, 200), (220, 200)]
direction = 'left'

# 定义食物的初始位置
food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

# 定义游戏循环标志
game_over = False

# 定义游戏循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # 移动贪吃蛇
    if direction == 'left':
        new_head = (snake[0][0] - 10, snake[0][1])
    elif direction == 'right':
        new_head = (snake[0][0] + 10, snake[0][1])
    elif direction == 'up':
        new_head = (snake[0][0], snake[0][1] - 10)
    elif direction == 'down':
        new_head = (snake[0][0], snake[0][1] + 10)

    # 检查是否撞墙或自撞
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        game_over = True
        break

    # 插入新的头部，并检查是否吃到食物
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
    else:
        snake.pop()

    # 绘制游戏界面
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, WHITE, (food[0], food[1], 10, 10))

    # 更新游戏界面
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(10)

# 退出Pygame
pygame.quit()
