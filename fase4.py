import pygame
import random
import math
from fase1 import dist, target_reached, out_of_bounds
import numpy as np

G_CONST = 10

def collision_planeta(state): # Função que verifica se o personagem colidiu com o planeta
    planeta_rect = pygame.Rect(state['buraco_negro_pos'][0], state['buraco_negro_pos'][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta_rect)

def update_state(state, assets):
    char_mass = state['char_mass']
    buraco_negro = state['buraco_negro_mass']
    char_pos = np.array(state['char_pos'])
    buraco_negro_pos = np.array(state['buraco_negro_pos'])
    char_vel = np.array(state['char_vel'])

    # calculate the distance and direction vector between the character and the planet
    r = buraco_negro_pos - char_pos
    r_norm = np.linalg.norm(r)
    r_hat = r / r_norm

    # calculate the gravitational force
    f_grav = (G_CONST * char_mass * buraco_negro) / (r_norm ** 2)

    # calculate the acceleration vector
    acc = f_grav * r_hat

    # update the character acceleration
    state['char_acc'] = acc

    # update the character position and velocity
    dt = 1 # time step
    state['char_pos'] = tuple(char_pos + char_vel * dt)
    state['char_vel'] = char_vel + acc * dt
    if collision_planeta(state): # Se o personagem colidir com o planeta, ele perde uma vida
        state['is_moving'] = False
        state['tela_atual'] = 'fase4'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0: # Se o personagem perder todas as vidas, ele perde o jogo
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif out_of_bounds(state): # Se o personagem sair da tela, ele perde uma vida
        state['is_moving'] = False
        state['tela_atual'] = 'fase4'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0: # Se o personagem perder todas as vidas, ele perde o jogo
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif target_reached(state): # Se o personagem chegar no planeta, ele ganha a fase
        sound_effect = pygame.mixer.Sound("wavs/RUSH-E-_vocals_-_mp3cut.net_.wav")
        sound_effect.play()
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        state['is_moving'] = False
        state['tela_atual'] = 'fase5_instrucoes'
        state['vidas'] = 5

def fase4_instructions(window, assets, state): # Função que mostra as instruções da fase
    img = pygame.image.load(assets['fase4_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Se o jogador apertar espaço, a fase começa
                state['tela_atual'] = 'fase4'

def fase4_game(window, assets, state): # Função que mostra a fase
    # caso a vida do personagem seja 3, a imagem da fase 3 vidas é carregada se a vida for 2, a imagem da fase 2 vidas é carregada e se a vida for 1, a imagem da fase 1 vida é carregada
    if state['vidas'] == 3:
        fase = pygame.image.load(assets['fases_3vidas']).convert()
        fase = pygame.transform.scale(fase, (1280, 720))
        window.blit(fase, (0, 0))
    elif state['vidas'] == 2:
        fase = pygame.image.load(assets['fases_2vidas']).convert()
        fase = pygame.transform.scale(fase, (1280, 720))
        window.blit(fase, (0, 0))
    elif state['vidas'] == 1:
        fase = pygame.image.load(assets['fases_1vidas']).convert()
        fase = pygame.transform.scale(fase, (1280, 720))
        window.blit(fase, (0, 0))
    character = pygame.image.load(assets['character']).convert_alpha()
    character = pygame.transform.scale(character, (75, 75))
    window.blit(character, (state['char_pos'][0], state['char_pos'][1]))
    planeta = pygame.image.load(assets['buraco_negro']).convert_alpha()
    planeta = pygame.transform.scale(planeta, (150, 150))
    window.blit(planeta, (state['buraco_negro_pos'][0], state['buraco_negro_pos'][1]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # Verifica se o jogador apertou a tecla enter para ir para o menu principal e reiniciar o jogo
                state['tela_atual'] = 'menu'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Verifica se o jogador apertou o botão esquerdo do mouse para lançar o personagem
            if event.button == 1 and not state['is_moving']: # Se o personagem não estiver se movendo, ele pode ser lançado
                # get mouse position
                mouse_pos = event.pos
                # launch the character in the direction of the mouse
                # calculate the angle between the character and the mouse
                angle = math.atan2(mouse_pos[1] - state['char_pos'][1], mouse_pos[0] - state['char_pos'][0])
                state['is_moving'] = True
                # calculate the velocity vector
                vel_x = 20 * math.cos(angle)
                vel_y = 20 * math.sin(angle)
                # launch the character with uniform velocity
                state['char_vel'] = (vel_x, vel_y)
                state['char_acc'] = (0, 0)
    if state['is_moving']: # Se o personagem estiver se movendo, ele é atualizado
        update_state(state, assets)