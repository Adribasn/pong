import pygame, sys
import random

screenWidth = 1024
screenHeight = 512

paddleHeight = 64
paddleWidth = 8
paddleGap = 24
paddleSpeed = 4

rightPaddleX = screenWidth - paddleGap - paddleWidth
rightPaddleY = int((screenHeight - paddleHeight) / 2)
rightPaddle = pygame.Rect(rightPaddleX, rightPaddleY, paddleWidth, paddleHeight)

leftPaddleX = paddleGap 
leftPaddleY = int((screenHeight - paddleHeight) / 2)
leftPaddle = pygame.Rect(leftPaddleX, leftPaddleY, paddleWidth, paddleHeight)

ballHeight = 16
ballWidth = 16
ballSpeedX = 5
ballSpeedY = random.randint(-5, 5)
ballX = int(screenWidth / 2) + 16
ballY = random.randint(0, screenHeight - ballHeight)
ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)

scoreLeft = 0
scoreRight = 0

collisionTolerance = 10

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

def drawRightPaddle():
    global paddleSpeed, screenHeight, paddleHeight

    if key[pygame.K_UP]:
        if (rightPaddle.y - paddleSpeed) > 0:
            rightPaddle.y -= paddleSpeed
        else:
            rightPaddle.y = 0
    if key[pygame.K_DOWN]:
        if (rightPaddle.y + paddleSpeed) < (screenHeight - paddleHeight):
            rightPaddle.y += paddleSpeed
        else:
            rightPaddle.y = screenHeight - paddleHeight
    
    pygame.draw.rect(screen, (255, 255, 255), rightPaddle)

def drawLeftPaddle():
    global paddleSpeed, screenHeight, paddleHeight

    if key[pygame.K_w]:
        if (leftPaddle.y - paddleSpeed) > 0:
            leftPaddle.y -= paddleSpeed
        else:
            leftPaddle.y = 0
    if key[pygame.K_s]:
        if (leftPaddle.y + paddleSpeed) < (screenHeight - paddleHeight):
            leftPaddle.y += paddleSpeed
        else:
            leftPaddle.y = screenHeight - paddleHeight

    pygame.draw.rect(screen, (255, 255, 255), leftPaddle)

def drawBouncingBall():
    global ballSpeedX, ballSpeedY, scoreLeft, scoreRight

    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1

    if ball.left <= 0:
        scoreRight += 1
        ball.x = int(screenWidth / 2) + 16
        ball.y = random.randint(0, screenHeight - ballHeight)

        ballSpeedX = 3
        ballSpeedY = random.randint(-5, 5)
    
    if ball.right >= screenWidth:
        scoreLeft += 1

        ball.x = int(screenWidth / 2) - ballWidth - 16
        ball.y = random.randint(0, screenHeight - ballHeight)

        ballSpeedX = -3
        ballSpeedY = random.randint(-5, 5)
    
    if ball.colliderect(rightPaddle):
        if abs(rightPaddle.left - ball.right) < collisionTolerance and ballSpeedX > 0:
            ballSpeedX *= -1
        if abs(rightPaddle.right - ball.left) < collisionTolerance and ballSpeedX < 0:
            ballSpeedX *= -1
        if abs(rightPaddle.top - ball.bottom) < collisionTolerance and ballSpeedY > 0:
            ballSpeedY *= -1
        if abs(rightPaddle.bottom - ball.top) < collisionTolerance and ballSpeedY < 0:
            ballSpeedY *= -1
    
    if ball.colliderect(leftPaddle):
        if abs(leftPaddle.right - ball.left) < collisionTolerance and ballSpeedX < 0:
            ballSpeedX *= -1
        if abs(leftPaddle.left - ball.right) < collisionTolerance and ballSpeedX > 0:
            ballSpeedX *= -1
        if abs(leftPaddle.top - ball.bottom) < collisionTolerance and ballSpeedY > 0:
            ballSpeedY *= -1
        if abs(leftPaddle.bottom - ball.top) < collisionTolerance and ballSpeedY < 0:
            ballSpeedY *= -1

    pygame.draw.rect(screen, (255, 255, 255), ball)

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
    drawBouncingBall()
    pygame.display.update()
    clock.tick(60)

