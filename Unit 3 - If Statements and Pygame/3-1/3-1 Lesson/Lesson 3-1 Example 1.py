# pygame1.py
# the basic template to draw a picture that is not moving

import pygame

# help(pygame)
pygame.init()  # ALL pygame programs need to initialize the pygame engine
# before they can use it

# Defining a colour constant(variables we should not be changing)
RED = (255, 0, 0)  # we use ALL CAPS for constants so we remember not to change them

SIZE = (800, 600)  # Open a pygame window
screen = pygame.display.set_mode(SIZE)

pygame.draw.line(screen, RED, (0, 0), (100, 50))  # draw our "scene"

pygame.event.get()
pygame.display.flip()  # pygame is designed for fast moving graphics if you
# don't use page flipping you can get a flickery mess
# basically Everything we draw is drawn in memory
# when we call flip() that picture gets copied to the
# screen

pygame.time.wait(3000)  # pause for three seconds so we can see it
pygame.quit()  # pygame likes to crash computers when you don't
# quit()


