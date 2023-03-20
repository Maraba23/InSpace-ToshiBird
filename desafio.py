import pygame
import random
import math
from fase1 import dist, target_reached, out_of_bounds
import numpy as np

G_CONST = 10

def collision_planeta(state): # Função que verifica se o personagem colidiu com o planeta
    planeta1_rect = pygame.Rect(state['planeta4_pos'][0][0], state['planeta4_pos'][0][1], 120, 120)
    planeta2_rect = pygame.Rect(state['planeta4_pos'][1][0], state['planeta4_pos'][1][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta1_rect) or char_rect.colliderect(planeta2_rect)

def desafio_instructions(window, assets, state): # Tela de instruções do desafio
    img = pygame.image.load(assets['desafio_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Se o usuário apertar espaço, a música muda e a tela atual muda para o desafio
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musicas/Dark souls.mp3")
                pygame.mixer.music.play(-1)
                state['tela_atual'] = 'desafio'
            elif event.key == pygame.K_RETURN: # Se o usuário apertar enter, a música muda e a tela atual muda para a tela de vitória sem desafio
                pygame.mixer.music.stop()
                sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
                sound_effect.play()
                state['tela_atual'] = 'win_no_challenge'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False

def update_state(state, assets): # Função que atualiza o estado do jogo
    char_mass = state['char_mass']
    planeta1_mass = state['planeta1_mass']
    planeta2_mass = state['planeta1_mass']
    char_pos = np.array(state['char_pos'])
    planeta1_pos = np.array(state['planeta4_pos'][0])
    planeta2_pos = np.array(state['planeta4_pos'][1])
    char_vel = np.array(state['char_vel'])

    r = dist(state['char_pos'], state['planeta4_pos'][0])
    r2 = dist(state['char_pos'], state['planeta4_pos'][1])
    r_norm = np.linalg.norm(r)
    r_norm2 = np.linalg.norm(r2)
    r_hat = r / r_norm
    r_hat2 = r2 / r_norm2
    f_grav = (G_CONST * char_mass * planeta1_mass) / (r_norm ** 2)
    f_grav2 = (G_CONST * char_mass * planeta2_mass) / (r_norm2 ** 2)

    acc = (f_grav * r_hat + f_grav2 * r_hat2) / char_mass
    state['char_acc'] = acc
    dt = 1
    state['char_vel'] = char_vel + acc * dt
    state['char_pos'] = char_pos + char_vel


    if target_reached(state): # Se o personagem chegar no alvo, a música muda e a tela atual muda para a tela de vitória com desafio
        pygame.mixer.music.stop()
        sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
        sound_effect.play()
        state['tela_atual'] = 'win_challenge'
    # check if the character is out of bounds
    if out_of_bounds(state): # Se o personagem sair da tela, a música muda e a tela atual muda para a tela de game over
        pygame.mixer.music.stop()
        pygame.mixer.music.load(assets['gameover_song'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        state['tela_atual'] = 'game_over'
    # check if the character collided with the planet
    if collision_planeta(state): # Se o personagem colidir com o planeta, a música muda e a tela atual muda para a tela de game over
        pygame.mixer.music.stop()
        pygame.mixer.music.load(assets['gameover_song'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        state['tela_atual'] = 'game_over'

def desafio_game(window, assets, state): # Função que desenha o desafio
    # o desafio nao tem vidas, apenas 1 tentativa
    if state['vidas'] == 5:
        fase = pygame.image.load(assets['fases_5vidas']).convert()
        fase = pygame.transform.scale(fase, (1280, 720))
        window.blit(fase, (0, 0))
    elif state['vidas'] == 4:
        fase = pygame.image.load(assets['fases_4vidas']).convert()
        fase = pygame.transform.scale(fase, (1280, 720))
        window.blit(fase, (0, 0))
    elif state['vidas'] == 3:
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
    window.blit(character, state['char_pos'])
    planeta1 = pygame.image.load(assets['planeta']).convert_alpha()
    planeta1 = pygame.transform.scale(planeta1, (100, 100))
    window.blit(planeta1, state['planeta4_pos'][0])
    planeta2 = pygame.image.load(assets['planeta']).convert_alpha()
    planeta2 = pygame.transform.scale(planeta2, (100, 100))
    window.blit(planeta2, state['planeta4_pos'][1])
    if state['planeta4_pos'][0][1] > 600:
        state['planeta4_vel'][0] = (0, -10)
    elif state['planeta4_pos'][0][1] < 100:
        state['planeta4_vel'][0] = (0, 10)
    if state['planeta4_pos'][1][1] > 600:
        state['planeta4_vel'][1] = (0, -10)
    elif state['planeta4_pos'][1][1] < 100:
        state['planeta4_vel'][1] = (0, 10)
    # update the planet position
    state['planeta4_pos'][0] = (state['planeta4_pos'][0][0] + state['planeta4_vel'][0][0], state['planeta4_pos'][0][1] + state['planeta4_vel'][0][1])
    state['planeta4_pos'][1] = (state['planeta4_pos'][1][0] + state['planeta4_vel'][1][0], state['planeta4_pos'][1][1] + state['planeta4_vel'][1][1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # Se o jogador apertar enter, a música muda e a tela atual muda para a tela de menu
                state['tela_atual'] = 'menu'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Se o jogador clicar com o mouse, o personagem é lançado na direção do mouse
            # o segredo do desafio eh poder se mover varias vezes, para facilitar o processo
            if event.button == 1:
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
    if state['is_moving']:
        update_state(state, assets)


