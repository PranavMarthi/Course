import pygame
import math

pygame.init()
SIZE = (800, 800)
screen = pygame.display.set_mode(SIZE)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.draw.rect(screen, RED, (0, 0, 800, 800))
pygame.draw.rect(screen, BLACK, (50, 50, 700, 700))
pygame.draw.line(screen, GREEN, (50, 50), (750, 750))
pygame.draw.line(screen, GREEN, (50, 750), (750, 50))

pygame.draw.arc(screen,(100, 200, 155), (50, 50, 200, 200), 0, math.pi)



pygame.event.get()
pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()
