import pygame, sys

screenWidth = 512 * 2
screenHeight = 256 * 2

def bouncingBall():
    return
    
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.KEY_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

