import pygame
from pygame.locals import*
from random import randint
import ctypes

ctypes.windll.kernel32.FreeConsole()

def on_grid_random():
    x = randint(0, 590)
    y = randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision_apple(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

font = pygame.font.SysFont('Arial', 18)
text = font.render('Você Perdeu!', True, (0, 255, 0))
textRect = text.get_rect()
textRect.center = (600//2, 600//2)

hight_pad = pygame.Rect(0, -10, 600, 0)#cima
left_pad = pygame.Rect(600, 0, 610, 600)#esquerda
down_pad = pygame.Rect(0, 600, 600, 610)#baixo
right_pad = pygame.Rect(-10, 0, 0, 600)#direita
pads = (hight_pad, left_pad, down_pad, right_pad)

my_direction = LEFT
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
         
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT
    if collision_apple(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
    
    head = pygame.Rect(snake_skin.get_clip())
    if head.collidelist(pads) >= 0:
        pygame.quit()
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    print(apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()
