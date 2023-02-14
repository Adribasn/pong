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

def drawRightPaddle():
    global rightPaddleY, paddleSpeed, screenHeight, paddleHeight

    if key[pygame.K_UP]:
        if (rightPaddleY - paddleSpeed) > 0:
            rightPaddleY -= paddleSpeed
        else:
            rightPaddleY = 0
    if key[pygame.K_DOWN]:
        if (rightPaddleY + paddleSpeed) < (screenHeight - paddleHeight):
            rightPaddleY += paddleSpeed
        else:
            rightPaddleY = screenHeight - paddleHeight
    
    pygame.draw.rect(screen, (255, 255, 255), (rightPaddleX, rightPaddleY, paddleWidth, paddleHeight))

def drawLeftPaddle():
    global leftPaddleY, paddleSpeed, screenHeight, paddleHeight

    if key[pygame.K_w]:
        if (leftPaddleY - paddleSpeed) > 0:
            leftPaddleY -= paddleSpeed
        else:
            leftPaddleY = 0
    if key[pygame.K_s]:
        if (leftPaddleY + paddleSpeed) < (screenHeight - paddleHeight):
            leftPaddleY += paddleSpeed
        else:
            leftPaddleY = screenHeight - paddleHeight

    pygame.draw.rect(screen, (255, 255, 255), (leftPaddleX, leftPaddleY, paddleWidth, paddleHeight))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ((screenWidth/2) - 3, 0, 6, screenHeight))
    drawRightPaddle()
    drawLeftPaddle()
    pygame.display.update()
    clock.tick(60)

