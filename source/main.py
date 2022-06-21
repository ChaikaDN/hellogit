import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.update()

#FIXME: pygame.error: video system not initialized
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
