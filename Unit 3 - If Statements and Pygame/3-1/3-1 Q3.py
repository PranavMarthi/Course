import pygame

pygame.init()
SIZE = (600, 600)
screen = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

location_box_x = int(input("Please enter the x coordinate of the box: "))
location_box_y = int(input("Please enter the y coordinate of the box: "))


def diagonals():
    pygame.draw.line(screen, WHITE, (location_box_x, location_box_y), (location_box_x + 70.71, location_box_y - 70.71),
                     5)
    pygame.draw.line(screen, WHITE, (location_box_x + 100, location_box_y),
                     (location_box_x + 100 + 70.71, location_box_y -
                      70.71), 5)
    pygame.draw.line(screen, WHITE, (location_box_x + 100, location_box_y + 100), (location_box_x + 100 + 70.71,
                                                                                   location_box_y + 100 - 70.71), 5)

    pygame.draw.line(screen, WHITE, (location_box_x + 70.71, location_box_y - 70.71), (location_box_x + 100 + 70.71,
                                                                                       location_box_y - 70.71), 5)
    pygame.draw.line(screen, WHITE, (location_box_x + 100 + 70.71, location_box_y -
                                     70.71), (location_box_x + 100 + 70.71, location_box_y + 100 - 70.71), 5)


pygame.draw.rect(screen, WHITE, (location_box_x, location_box_y, 100, 100), 5)

pygame.event.get()
pygame.display.flip()
pygame.time.wait(1)

diagonals()

pygame.event.get()
pygame.display.flip()
pygame.time.wait(10000)

pygame.quit()
