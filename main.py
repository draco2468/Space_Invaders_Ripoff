import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1250,650))

pygame.display.set_caption("Spce Invaders' Ripoff")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #checks if you quit the game
            running = False