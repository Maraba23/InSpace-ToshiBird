import pygame
import numpy as np
import random
from menu import main_menu, story_screen, instructions_screen

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 860
BLACK = (0, 0, 0)

assets = {'width': SCREEN_WIDTH,
          'height': SCREEN_HEIGHT,
          'background': 'images/background.png',
          'menu1': 'images/main_menu1.png',
          'menu2': 'images/main_menu2.png',
          'menu3': 'images/main_menu3.png',
          'menu4': 'images/main_menu4.png',
          'story': 'images/story.png',
          'instructions': 'images/instructions.png',
          'e_sound': 'musicas/RUSH E [vocals] (mp3cut.net).mp3'}

pygame.mixer.init()
pygame.mixer.music.load(assets['e_sound'])

telas = ['menu', 'story', 'instructions', 'fase1', 'fase2', 'fase3', 'fase4', 'desafio', 'game_over', 'win']

state = {'tela_atual': 'menu',
         'quit': False,
         'perdeu': False,
         'telas': telas,
         'ganhou': False}

'''window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

personagens = ["images/personagem_soos.jpeg", "images/personagem_soos2.jpeg"]
personagem = pygame.image.load(random.choice(personagens))
personagem = pygame.transform.scale(personagem, (50, 50))

planeta = pygame.image.load("images/planeta-removebg-preview.png")
planeta = pygame.transform.scale(planeta, (120, 100))

planeta_pos_x, planeta_pos_y = random.randint(SCREEN_WIDTH * 0.1, SCREEN_WIDTH * 0.9), random.randint(
    SCREEN_HEIGHT * 0.05, SCREEN_HEIGHT * 0.95)'''

def gameloop(state, assets):
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("InSpace Toshi Bird")
    clock = pygame.time.Clock()
    FPS = 24

    while True:
        print(state['tela_atual'])
        if state['tela_atual'] == 'menu':
            main_menu(window, assets, state)
        elif state['tela_atual'] == 'story':
            story_screen(window, assets, state)
        elif state['tela_atual'] == 'instructions':
            instructions_screen(window, assets, state)
        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    gameloop(state, assets)


