import pygame
from pygame.draw import *
from random import randint
pygame.init()

'''
Суть игры проста: в случайном месте появляется на короткое время шарик,
и мы должны успеть щелкнуть по нему мышкой.
'''

FPS = 0.8
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

'''
def new_ball():
    """рисует новый шарик """
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
'''
font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
xc = 0
yc = 0
while not finished:
    clock.tick(FPS)

    draw_text(screen, str(score), 50, 600, 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            xc = (event.pos[0])
            yc = (event.pos[1])
            print(xc)
            print(yc)
            # print(type(event.pos))

    new_ball()
    pygame.display.update()
    c = (((xc - x)**2) + ((yc - y)**2))**0.5
    d = ((xc - x))
    e = ((xc - x)**2)
    print("c: ", c)
    print("d: ", d)
    print("e: ", e)
    if c <= r:
        score += 1
        print("Попал!")
    else:
        print("Мимо!")

    print(x, y, r)

    screen.fill(BLACK)

pygame.quit()
