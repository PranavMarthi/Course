import pygame

pygame.init()
SIZE = (500, 500)
screen = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

BLUE = (0, 0, 255)


w, h = pygame.display.get_surface().get_size()
print(w, h)

W = int((int(w) - 100) / 2)
H = int((int(h) - 100) / 2)


pygame.draw.rect(screen, BLUE, (0, 0, w, h))


pygame.draw.rect(screen, BLACK, (W, H, 100, 100))

pygame.event.get()
pygame.display.flip()
pygame.time.wait(10000)

pygame.quit()