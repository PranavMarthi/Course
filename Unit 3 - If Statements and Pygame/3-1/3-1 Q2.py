# https://www.pygame.org/docs/
import os
import pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 20)

pygame.init()
SIZE = (600, 600)
screen = pygame.display.set_mode(SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def drawScreen():
    pygame.draw.line(screen, WHITE, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, WHITE, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, WHITE, (0, 400), (600, 400), 5)


def drawCross(x_position, y_position):
    pygame.draw.line(screen, WHITE, (x_position, y_position), (x_position + 100, y_position + 100), 5)
    pygame.draw.line(screen, WHITE, (x_position + 100, y_position), (x_position, y_position + 100), 5)


def drawCircle(x_position, y_position):
    pygame.draw.circle(screen, WHITE, (x_position, y_position), 50, 5)


drawScreen()
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCross(50, 50)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCircle(300, 300)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCross(50, 250)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCircle(100, 500)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)


drawCross(450, 50)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)


drawCircle(500, 300)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)


drawCross(250, 450)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCircle(300, 100)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

drawCross(450, 450)
pygame.event.get()
pygame.display.flip()
pygame.time.wait(1000)

pygame.quit()
