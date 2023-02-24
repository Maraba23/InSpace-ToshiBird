import pygame
import numpy as np
import random
from menu import main_menu, story_screen, instructions_screen
from fase1 import fase1_instructions, fase1_game
from fase2 import fase2_instructions, fase2_game
from gameover import game_over_screen
from fase3 import fase3_instructions, fase3_game
from fase4 import fase4_game, fase4_instructions
from fase5 import fase5_game, fase5_instructions

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)

planeta_pos_x, planeta_pos_y = random.randint(SCREEN_WIDTH * 0.3, SCREEN_WIDTH * 0.7), random.randint(SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.6)

planeta1_x, planeta1_y, planeta2_x, planeta2_y = random.randint(SCREEN_WIDTH * 0.3, SCREEN_WIDTH * 0.7), random.randint(SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.6), random.randint(SCREEN_WIDTH * 0.3, SCREEN_WIDTH * 0.7), random.randint(SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.6)

assets = {'width': SCREEN_WIDTH,
          'height': SCREEN_HEIGHT,
          'gameover': 'images/gameover.png',
          'background': 'images/background.png',
          'menu1': 'images/main_menu1.png',
          'menu2': 'images/main_menu2.png',
          'menu3': 'images/main_menu3.png',
          'menu4': 'images/main_menu4.png',
          'story': 'images/story.png',
          'instructions': 'images/instructions.png',
          'e_sound': 'musicas/RUSH E [vocals] (mp3cut.net).mp3',
          'gameover_song': 'musicas/morre.mp3',
          'giorno' : 'musicas/Giorno.mp3',
          'fases_3vidas': 'images/fases_3vidas.png',
          'fases_2vidas': 'images/fases_2vidas.png',
          'fases_1vidas': 'images/fases_1vidas.png',
          'character': 'images/toshi.png',
          'planeta': 'images/planeta.png',
          'fase1_instrucoes': 'images/fase1_instrucoes.png',
          'fase2_instrucoes': 'images/fase2_instrucoes.png',
          'fase3_instrucoes': 'images/fase3_instrucoes.png'}

telas = ['menu', 'story', 'instructions', 'fase1_instrucoes', 'fase1', 'fase2', 'fase3', 'fase4', 'desafio', 'game_over', 'win']

state = {'tela_atual': 'menu',
         'quit': False,
         'perdeu': False,
         'telas': telas,
         'ganhou': False,
         'vidas': 3,
         'planeta1_pos': (610, 430),
         'planeta2_pos': (planeta_pos_x, planeta_pos_y),
         'planeta3_pos': ((planeta1_x, planeta1_y), (planeta2_x, planeta2_y)),
         'planeta1_mass': 1500,
         'planeta2_mass': 1000,
         'char_pos': (int(75/2), int(assets['height']/2)),
         'char_vel': (0, 0),
         'char_acc': (0, 0),
         'char_mass': 1,
         'is_moving': False,
         'target_pos': ((1190, 196), (1280, 305))}

pygame.init()
pygame.mixer.init(frequency=44100, size=-16)
pygame.mixer.music.load(assets['e_sound'])
pygame.mixer.music.set_volume(0.5)

sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
sound_effect_e = pygame.mixer.Sound("wavs/RUSH-E-_vocals_-_mp3cut.net_.wav")

def gameloop(state, assets):
    pygame.mixer.music.play()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("InSpace Toshi Bird")
    clock = pygame.time.Clock()
    FPS = 1000

    while True:
        if state['tela_atual'] == 'menu':
            main_menu(window, assets, state)
        elif state['tela_atual'] == 'story':
            story_screen(window, assets, state)
        elif state['tela_atual'] == 'instructions':
            instructions_screen(window, assets, state)
        elif state['tela_atual'] == 'fase1_instrucoes':
            fase1_instructions(window, assets, state)
        elif state['tela_atual'] == 'fase1':
            fase1_game(window, assets, state)
        elif state['tela_atual'] == 'fase2_instrucoes':
            fase2_instructions(window, assets, state)
        elif state['tela_atual'] == 'fase2':
            fase2_game(window, assets, state)
        elif state['tela_atual'] == 'game_over':
            game_over_screen(window, state, assets)
        elif state['tela_atual'] == 'fase3_instrucoes':
            fase3_instructions(window, assets, state)
        elif state['tela_atual'] == 'fase3':
            fase3_game(window, assets, state)
        elif state['tela_atual'] == 'fase4':
            fase4_game(window, assets, state)
        elif state['tela_atual'] == 'fase4_instrucoes':
            fase4_instructions(window, assets, state)
        elif state['tela_atual'] == 'fase5':
            fase5_game(window, assets, state)
        elif state['tela_atual'] == 'fase5_instrucoes':
            fase5_instructions(window, assets, state)
        

        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    gameloop(state, assets)


