# the following code will always put the screen in the top corner
import os
import random
import pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

pygame.init()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)

for i in range(0, 501, 5):

    for j in range(0, 501, 5):
        colour = random.choice([(255, 0, 0), (0, 0, 255), (0, 255, 0)])
        pygame.draw.rect(screen, colour, (j, i, 5, 5))

pygame.event.get()
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
