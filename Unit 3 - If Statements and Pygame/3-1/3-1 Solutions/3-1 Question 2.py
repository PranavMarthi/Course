# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

# pygame2a.py
# draw a face using a few of the pygame draw methods

import pygame   
pygame.init()
#defining colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)

waitTime = 2500

#background
pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))

#horizontal lines
pygame.draw.line(screen, BLACK, (160, 240), (640, 240),5)
pygame.draw.line(screen, BLACK, (160, 360), (640, 360),5)

#vertical lines
pygame.draw.line(screen, BLACK, (320, 120), (320, 480),5)
pygame.draw.line(screen, BLACK, (480, 120), (480, 480),5)

#draw first X
pygame.draw.line(screen, RED, (320, 240), (480, 360),5)
pygame.draw.line(screen, RED, (320, 360), (480, 240),5)
pygame.display.flip()
pygame.time.wait(waitTime)

#draw first O
pygame.draw.circle(screen, BLUE, (560, 180), 60, 5)
pygame.display.flip()
pygame.time.wait(waitTime)

#draw second X
pygame.draw.line(screen, RED, (480, 360), (640, 480),5)
pygame.draw.line(screen, RED, (480, 480), (640, 360),5)

pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
