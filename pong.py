import pygame, sys

screenWidth = 1024
screenHeight = 512

paddleHeight = 64
paddleWidth = 8
paddleGap = 24
paddleSpeed = 3

rightPaddleX = screenWidth - paddleGap - paddleWidth
rightPaddleY = int((screenHeight - paddleHeight) / 2)

leftPaddleX = paddleGap 
leftPaddleY = int((screenHeight - paddleHeight) / 2)
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP]:
        rightPaddleY -= paddleSpeed
    if key[pygame.K_DOWN]:
        rightPaddleY += paddleSpeed

    if key[pygame.K_w]:
        leftPaddleY -= paddleSpeed
    if key[pygame.K_s]:
        leftPaddleY += paddleSpeed
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ((screenWidth/2) - 3, 0, 6, screenHeight))
    pygame.draw.rect(screen, (255, 255, 255), (rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))
    pygame.draw.rect(screen, (255, 255, 255), (leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))
    pygame.display.update()
    clock.tick(60)

