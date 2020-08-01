import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders' Ripoff")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load("player.png")
playerX = 368
playerY = 443
playerX_change = 0

enemyImage = pygame.image.load("enemy.png")
#game loop
running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #checks if you quit the game
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX = playerX + playerX_change
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736
    screen.blit(playerImage, (playerX, playerY))
    pygame.display.update()