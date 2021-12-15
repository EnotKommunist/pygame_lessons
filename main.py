import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen = pygame.display.set_mode((600, 600))
running = True
cell_Life = False
image = load_image('arrow.png')
screen.blit(image, (350, 350))
fps = 10
clock = pygame.time.Clock()
cords_mouse = (None, None)
pygame.mouse.set_visible(False)
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cords_mouse = event.pos
    if cords_mouse[0] and pygame.mouse.get_focused():
        screen.blit(image, cords_mouse)
    pygame.display.flip()