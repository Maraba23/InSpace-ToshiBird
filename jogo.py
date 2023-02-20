import pygame
import numpy as np
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 860
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# set caption
pygame.display.set_caption("InSpace Toshi Bird")
FPS = 60

personagens = ["images/personagem_soos.jpeg", "images/personagem_soos2.jpeg"]
personagem = pygame.image.load(random.choice(personagens))
personagem = pygame.transform.scale(personagem, (50, 50))

planeta = pygame.image.load("images/planeta-removebg-preview.png")
planeta = pygame.transform.scale(planeta, (120, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(BLACK)
    screen.blit(personagem, (0, SCREEN_HEIGHT * 0.5))
    screen.blit(planeta, (planeta_pos_x, planeta_pos_y))
    pygame.display.update()
    clock.tick(FPS)