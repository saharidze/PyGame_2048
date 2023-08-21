"""
Body of game
"""
import pygame.transform

from database import *
from logic import *

GAMERS_DB = get_best()


def draw_intro():
    img2048 = pygame.image.load("Intro.jpg")
    font = pygame.font.SysFont("stxinkai", 70)
    text_welcome = font.render("Здарова", True, WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.blit(pygame.transform.scale(img2048, [200, 200]), (10, 10))
        screen.blit(text_welcome, (250, 60))
        pygame.display.update()


def draw_top_gaymers():
    font_top = pygame.font.SysFont("simsun", 30)
    font_gaymer = pygame.font.SysFont("simsun", 24)
    text_head = font_top.render(f"TryHards", True, BLACK)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{index+1}. {name} - {score}"
        text_gamer = font_gaymer.render(s, True, BLACK)
        screen.blit(text_gamer, (250, 30 + 25 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
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
    pretty_print(mas)
    draw_top_gaymers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f"{value}", True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_w) / 2
                screen.blit(text, (text_x, text_y))


mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 128, 0),
    32: (255, 0, 0),
    64: (128, 0, 0),
    128: (255, 255, 255),
    256: (255, 255, 128),
    512: (255, 255, 0),
    1024: (255, 128, 0),
    2048: (255, 0, 0),
    4096: (128, 0, 0),
    8192: (255, 255, 255),
    16384: (255, 255, 128),
    32768: (255, 255, 0),
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
score = 0
mas[1][2] = 2
mas[3][0] = 4

# for gaymer in get_best():
#     print(gaymer)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

draw_intro()
draw_interface(score)
pygame.display.update()

while is_zero_in_mas(mas) and can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            if event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            if event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            if event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            draw_interface(score, delta)
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            insert_2_or_4(mas, x, y)
            pygame.display.update()
