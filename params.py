import pygame
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