# the following code will always put the screen in the top corner
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (20, 20)

# pygame2a.py
# draw a face using a few of the pygame draw methods

import pygame

pygame.init()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)

# Draws a red face
pygame.draw.circle(screen, RED, (200, 100), 50)
pygame.draw.circle(screen, BLACK, (185, 70), 5)  # Left eye
pygame.draw.circle(screen, BLACK, (215, 70), 5)  # Right eye
pygame.draw.line(screen, BLACK, (185, 85), (215, 85))  # Mouth

pygame.event.get()
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
