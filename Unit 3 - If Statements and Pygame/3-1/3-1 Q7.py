import pygame

pygame.init()
SIZE = (500, 500)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode(SIZE)
w, h = pygame.display.get_surface().get_size()
W = int(w)
H = int(h)

placement_X = W/2 - 75
placement_Y = H/2 - 75

pygame.draw.rect(screen, WHITE, (0, 0, W, H))
pygame.draw.ellipse(screen, BLACK, (int(placement_X), int(placement_Y), 150, 150))
pygame.draw.ellipse(screen, YELLOW, (int(placement_X) + 5, int(placement_Y) + 5, 140, 140))
pygame.draw.ellipse(screen, BLACK, (int(placement_X) + 75, int(placement_Y) + 50, 15, 15))

# pygame.draw.polygon(screen, WHITE, )

pygame.event.get()
pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
