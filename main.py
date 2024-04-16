# Maksymilian Szulc 1A - SANDBOX
# How to use SANDBOX?
# Key E: Set Brush to EMPTY
# Key F: Set Brush to SNOW
# Key R: Set Brush to ROCK
# Key S: Set Brush to SAND
# Key T: Set Brush to TOXIC
import random
import pygame
import os
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 800
tile_size = 15
rows = screen_height // tile_size
columns = screen_width // tile_size
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sandbox")
clock = pygame.time.Clock()

EMPTY = 0
SAND = 1
ROCK = 2
TOXIC = 3
SNOW = 4


board = [[EMPTY for c in range(columns)] for r in range(rows)]
brush = SAND
running = True
placing_block = False
pygame.font.init()
path = os.path.join(os.path.dirname(__file__), "font.ttf")
font = pygame.font.Font(path, 30)
instructions = [
    "Key E: Set Brush to EMPTY",
    "Key F: Set Brush to SNOW",
    "Key R: Set Brush to ROCK",
    "Key S: Set Brush to SAND",
    "Key T: Set Brush to TOXIC"
]
while running:
    clock.tick(fps)
    screen.fill((0, 0, 0))



    y_offset = 10
    for instr in instructions:
        text_surface = font.render(instr, True, (255, 255, 255))
        screen.blit(text_surface, (screen_width - text_surface.get_width() - 10, y_offset))
        y_offset += text_surface.get_height() + 5

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                placing_block = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                placing_block = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                brush = SAND
            if event.key == pygame.K_r:
                brush = ROCK
            if event.key == pygame.K_e:
                brush = EMPTY
            if event.key == pygame.K_t:
                brush = TOXIC
            if event.key == pygame.K_f:
                brush = SNOW

    if placing_block:
        x, y = pygame.mouse.get_pos()
        r = y // tile_size
        c = x // tile_size
        if 0 <= r < rows and 0 <= c < columns:
            board[r][c] = brush
    for index in range(rows - 1):
        for column in range(columns):
            row = rows - 2 - index
            if board[row][column] == SAND:
                if board[row + 1][column] == EMPTY:
                    board[row][column] = EMPTY
                    board[row + 1][column] = SAND
                else:
                    if random.randint(0, 100) < 50:
                        if column - 1 >= 0 and board[row + 1][column - 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column - 1] = SAND
                        elif column + 1 < columns and board[row + 1][column + 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column + 1] = SAND
                    else:
                        if column + 1 < columns and board[row + 1][column + 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column + 1] = SAND
                        elif column - 1 >= 0 and board[row + 1][column - 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column - 1] = SAND

            elif board[row][column] == TOXIC:
                if row + 1 < rows and (board[row + 1][column] == EMPTY or board[row + 1][column] == SAND):
                    if board[row + 1][column] == SAND:
                        board[row + 1][column] = TOXIC
                    else:
                        if column - 1 >= 0 and random.randint(0, 100) < 50:
                            board[row][column] = EMPTY
                            board[row + 1][column - 1] = TOXIC
                        elif column + 1 < columns and random.randint(0, 100) < 50:
                            board[row][column] = EMPTY
                            board[row + 1][column + 1] = TOXIC
                        else:
                            board[row][column] = EMPTY
                            if row - 1 >= 0:
                                board[row - 1][column] = TOXIC
                else:
                    if random.randint(0, 100) < 50:
                        if column - 1 >= 0 and board[row + 1][column - 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column - 1] = TOXIC
                        elif column + 1 < columns and board[row + 1][column + 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column + 1] = TOXIC
                    else:
                        if column + 1 < columns and board[row + 1][column + 1] == EMPTY:
                            board[row][column] = EMPTY
                            board[row + 1][column + 1] = TOXIC
                        elif column - 1 >= 0 and board[row + 1][column - 1] == EMPTY:
                            board[row][column] = EMPTY
                            if row - 1 >= 0:
                                board[row - 1][column] = TOXIC




    for row in range(rows - 1, 0, -1):
        for column in range(columns):
            if board[row][column] == SNOW:
                if row + 1 < rows and board[row + 1][column] == EMPTY:
                    board[row][column] = EMPTY
                    board[row + 1][column] = SNOW


    for row in range(rows):
        for column in range(columns):
            if board[row][column] == SAND:
                        pygame.draw.rect(screen, (255, 235, 59),
                                         (column * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][column] == ROCK:
                        pygame.draw.rect(screen, (169, 169, 169),
                                         (column * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][column] == TOXIC:
                        pygame.draw.rect(screen, (0, 100, 0),
                                         (column * tile_size, row * tile_size, tile_size, tile_size))
            elif board[row][column] == SNOW:
                        pygame.draw.rect(screen, (255, 255, 255),
                                         (column * tile_size, row * tile_size, tile_size, tile_size))

    pygame.display.update()

pygame.quit()
