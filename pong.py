import pygame, sys
import random
import math

screenWidth = 1024
screenHeight = 512

paddleHeight = 64
paddleWidth = 12
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

while True:
    ballSpeedX = random.randint(0, 7)
    ballSpeedY = random.randint(-5, 5)
    if 6 < math.sqrt(pow(ballSpeedX, 2) + pow(ballSpeedY, 2)) < 7:
        break
    
ballX = int(screenWidth / 2) + 16
ballY = random.randint(0, screenHeight - ballHeight)
ball = pygame.Rect(ballX, ballY, ballWidth, ballHeight)

scoreLeft = 0
scoreRight = 0

collisionTolerance = 10

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
textFont = pygame.font.Font("assets/bit5x3.ttf", 120)
hitSound = pygame.mixer.Sound("assets\hit.wav")
hitSound.set_volume(.5)
bounceSound = pygame.mixer.Sound("assets/blip.wav")
bounceSound.set_volume(.25)

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

    playBounce = False

    if ball.top <= 0 or ball.bottom >= screenHeight:
        bounceSound.play()
        ballSpeedY *= -1

    if ball.left <= 0:
        hitSound.play()
        scoreRight += 1
        
        ball.x = int(screenWidth / 2) - ballWidth - 16
        ball.y = random.randint(0, screenHeight - ballHeight)

        while True:
            ballSpeedX = random.randint(-7, 0)
            ballSpeedY = random.randint(-5, 5)
            if 6 < math.sqrt(pow(ballSpeedX, 2) + pow(ballSpeedY, 2)) < 7:
                break
    
    if ball.right >= screenWidth:
        hitSound.play()
        scoreLeft += 1

        ball.x = int(screenWidth / 2) + 16
        ball.y = random.randint(0, screenHeight - ballHeight)

        while True:
            ballSpeedX = random.randint(0, 7)
            ballSpeedY = random.randint(-5, 5)
            if 6 < math.sqrt(pow(ballSpeedX, 2) + pow(ballSpeedY, 2)) < 7:
                break
    
    if ball.colliderect(rightPaddle):
        playSound = False
        if abs(rightPaddle.left - ball.right) < collisionTolerance and ballSpeedX > 0:
            playSound = True
            ballSpeedX *= -1
        if abs(rightPaddle.right - ball.left) < collisionTolerance and ballSpeedX < 0:
            playSound = False
            ballSpeedX *= -1
        if abs(rightPaddle.top - ball.bottom) < collisionTolerance and ballSpeedY > 0:
            playSound = False
            ballSpeedY *= -1
        if abs(rightPaddle.bottom - ball.top) < collisionTolerance and ballSpeedY < 0:
            playSound = False
            ballSpeedY *= -1
        
        if playSound:
            bounceSound.play()
    
    if ball.colliderect(leftPaddle):
        playSound = False
        if abs(leftPaddle.right - ball.left) < collisionTolerance and ballSpeedX < 0:
            playSound = True
            ballSpeedX *= -1
        if abs(leftPaddle.left - ball.right) < collisionTolerance and ballSpeedX > 0:
            playSound = True
            ballSpeedX *= -1
        if abs(leftPaddle.top - ball.bottom) < collisionTolerance and ballSpeedY > 0:
            playSound = True
            ballSpeedY *= -1
        if abs(leftPaddle.bottom - ball.top) < collisionTolerance and ballSpeedY < 0:
            playSound = True
            ballSpeedY *= -1

        if playSound:
            bounceSound.play()

    pygame.draw.circle(screen, (255, 255, 255), (ball.x + (ballWidth/2), ball.y + (ballHeight/2)), ballWidth/2)

def drawScore():
    global scoreLeft, scoreRight
    
    if scoreLeft > 99:
        scoreLeft = 99

    if scoreLeft < 10:
        scoreLeftDisplay = textFont.render("0" + str(scoreLeft), 1, (255, 255, 255))
        screen.blit(scoreLeftDisplay, ((screenWidth / 2) - 125, 15))
    else:
        scoreLeftDisplay = textFont.render(str(scoreLeft), 1, (255, 255, 255))
        screen.blit(scoreLeftDisplay, ((screenWidth / 2) - 125, 15))

    if scoreRight > 99:
        scoreRight = 99

    if scoreRight < 10:
        scoreRightDisplay = textFont.render("0" + str(scoreRight), 1, (255, 255, 255))
        screen.blit(scoreRightDisplay, ((screenWidth / 2) + 20, 15))
    else:
        scoreRightDisplay = textFont.render(str(scoreRight), 1, (255, 255, 255))
        screen.blit(scoreRightDisplay, ((screenWidth / 2) + 20, 15))

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
    drawScore()
    pygame.display.update()
    clock.tick(60)

