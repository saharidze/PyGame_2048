"""
Body of game
"""
import random
import sys

import pygame
import pygame.transform

from database import get_best, insert_result
from logic import (can_move, get_empty_list, get_index_from_number,
                   insert_2_or_4, is_zero_in_mas, move_down, move_left,
                   move_right, move_up)
from params import (BLACK, BLOCKS, COLORS, HEIGHT, MARGIN, SIZE_BLOCK,
                    TITLE_REC, WHITE, WIDTH)

GAMERS_DB = get_best()
USERNAME = None


def init_const():
    """Инициализация поля и счёта"""
    global score, mas
    mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0


mas = None
score = None
init_const()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def draw_intro():
    """Прорисовка заставки"""
    img2048 = pygame.image.load("Intro.jpg")
    font = pygame.font.SysFont("stxinkai", 70)
    text_welcome = font.render("Здарова", True, WHITE)
    name = ""
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        screen.blit(pygame.transform.scale(img2048, [200, 200]), (10, 10))
        screen.blit(text_welcome, (250, 60))
        text_name = font.render(name, True, WHITE)
        react_name = text_name.get_rect()
        react_name.center = screen.get_rect().center
        screen.blit(text_name, react_name)
        pygame.display.update()
    print(USERNAME)


def draw_top_gaymers():
    """Прорисовка поля рекордов"""
    font_top = pygame.font.SysFont("simsun", 30)
    font_gaymer = pygame.font.SysFont("simsun", 24)
    text_head = font_top.render("TryHards", True, BLACK)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        score_string = f"{index + 1}. {name} - {score}"
        text_gamer = font_gaymer.render(score_string, True, BLACK)
        screen.blit(text_gamer, (250, 30 + 25 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
    """Прорисовка основного поля"""
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("simsun", 48)
    font_delta = pygame.font.SysFont("simsun", 24)
    text_score = font_score.render("Score", True, BLACK)
    text_score_value = font_score.render(f"{score}", True, BLACK)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, BLACK)
        screen.blit(text_delta, (175, 85))
    draw_top_gaymers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f"{value}", True, BLACK)
            width = column * SIZE_BLOCK + (column + 1) * MARGIN
            height = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (width, height, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = width + (SIZE_BLOCK - font_w) / 2
                text_y = height + (SIZE_BLOCK - font_w) / 2
                screen.blit(text, (text_x, text_y))


def draw_gameover():
    """Прорисовка после завершения игры"""
    global USERNAME, mas, score
    img2048 = pygame.image.load("Intro.jpg")
    font = pygame.font.SysFont("stxinkai", 70)
    text_gameover = font.render("ББ", True, WHITE)
    text_score = font.render(f"{score}", True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "New Record"
        text_record = font.render(text, True, WHITE)
    else:
        text = "Nope"
        text_record = font.render(text, True, WHITE)
    insert_result(USERNAME, score)
    make_disigion = False
    while not make_disigion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # restart game with name
                    make_disigion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart without name
                    USERNAME = None
                    make_disigion = True
                    init_const()

        screen.fill(BLACK)
        screen.blit(text_gameover, (230, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), (10, 10))
        pygame.display.update()
    screen.fill(BLACK)


def game_loop():
    """Основная механика игры"""
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_button_click = False
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                    is_button_click = True
                if event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)
                    is_button_click = True
                if event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                    is_button_click = True
                if event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)
                    is_button_click = True
                score += delta
                if is_zero_in_mas(mas) and is_button_click is True:
                    draw_interface(score, delta)
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    insert_2_or_4(mas, x, y)
                    is_button_click = False
                pygame.display.update()


while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_gameover()
