import pygame
from pygame.draw import *
# после импорта библиотеки, необходимо её инициализировать:
pygame.init()

FPS = 30
# И создать окно:
screen = pygame.display.set_mode((300, 200))

# здесь будут рисоваться фигуры

# ...

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.

clock = pygame.time.Clock()

while True:
	clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
