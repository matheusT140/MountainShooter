import pygame

print('Setup start')
pygame.init()
screen = pygame.display.set_mode(size=(800, 600))
print('Setup end')

print('Loop start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close screen
            print('Loop end')
            quit() # end pygame
