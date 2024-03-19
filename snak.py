
import pygame
import time
import random

pygame.init()

# Ukuran layar
width = 800
height = 600

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Jendela game
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

block_size = 20
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [width / 2 - screen_text.get_width() / 2, height / 2 - screen_text.get_height() / 2])

def gameLoop():
    game_over = False
    game_close = False

    lead_x = width / 2
    lead_y = height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    randAppleX = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            win.fill(white)
            message_to_screen('Game Over, press Q-Quit or C-Play Again', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        win.fill(white)
        pygame.draw.rect(win, red, [randAppleX, randAppleY, block_size, block_size])

        snake_Head = []
        snake_Head.append(lead_x)
        snake_Head.append(lead_y)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()

