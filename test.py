import pygame

from pygame.locals import *

from shape2d import shape2d

# boot
pygame.init()
pygame.font.init()

# for throttling and tracking FPS
fps = pygame.time.Clock()

FPS_LIMIT = 60

# we'll use SCREEN_WIDTH and SCREEN_HEIGHT for coordinate translation 
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# pygame needs a tuple for creating its window, so pack those up
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# create screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# load the shape we want to draw
shape = shape2d('ship.2')

# core loop
QUIT = False

def origin_convert(vertex):
    x, y = vertex[0], vertex[1]
    x1 =  x + SCREEN_WIDTH / 2
    y1 = -y + SCREEN_HEIGHT / 2

    return (x1, y1)

while not QUIT:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.mod == pygame.KMOD_NONE:
                pass
            # all of our key bindings go here
            if event.key == pygame.K_ESCAPE:
                QUIT = True

            # WASD for shape translation
            if event.key == pygame.K_w:
                shape.translate(0, -5)
            if event.key == pygame.K_a:
                shape.translate(-5, 0)
            if event.key == pygame.K_s:
                shape.translate(0, 5)
            if event.key == pygame.K_d:
                shape.translate(5, 0)

            # scaling with z/c
            if event.key == pygame.K_z:
                shape.scale(0.95)
            if event.key == pygame.K_c:
                shape.scale(1.05)

            # rotation with q/e
            if event.key == pygame.K_q:
                shape.rotate(15)
            if event.key == pygame.K_e:
                shape.rotate(-15)

    screen.fill(pygame.Color(0,0,0))

    # draw the loaded shape
    shape.draw(screen)

    pygame.display.update()
    fps.tick(FPS_LIMIT)
