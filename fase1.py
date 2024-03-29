import pygame
import random
import math
import numpy as np

G_CONST = 10

def dist(p1, p2): # Calcula a distância entre dois pontos
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def target_reached(state): # Verifica se o personagem chegou no alvo
    target_rect = pygame.Rect(state['target_pos'][0][0], state['target_pos'][0][1], state['target_pos'][1][0] - state['target_pos'][0][0], state['target_pos'][1][1] - state['target_pos'][0][1])
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(target_rect)

def collision_planeta(state): # Verifica se o personagem colidiu com os planetas
    planeta_rect = pygame.Rect(state['planeta1_pos'][0], state['planeta1_pos'][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta_rect)

def out_of_bounds(state): # Verifica se o personagem saiu da tela
    return state['char_pos'][0] < 0 or state['char_pos'][0] > 1280 or state['char_pos'][1] < 0 or state['char_pos'][1] > 860

def update_state(state, assets):
    char_mass = state['char_mass']
    planeta1_mass = state['planeta1_mass']
    char_pos = np.array(state['char_pos'])
    planeta1_pos = np.array(state['planeta1_pos'])
    char_vel = np.array(state['char_vel'])

    # calculate the distance and direction vector between the character and the planet
    r = planeta1_pos - char_pos
    r_norm = np.linalg.norm(r)
    r_hat = r / r_norm

    # calculate the gravitational force
    f_grav = (G_CONST * char_mass * planeta1_mass) / (r_norm ** 2)

    # calculate the acceleration vector
    acc = r_hat * f_grav

    # update the character acceleration
    state['char_acc'] = acc

    # update the character position and velocity
    dt = 1 # time step
    state['char_pos'] = tuple(char_pos + char_vel * dt)
    state['char_vel'] = char_vel + acc * dt

    # check for collisions and out of bounds
    if collision_planeta(state) or out_of_bounds(state):
        state['is_moving'] = False
        state['tela_atual'] = 'fase1'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0: # Verifica se o personagem perdeu todas as vidas e vai para a tela de game over
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif target_reached(state): # Usa a função target_reached para verificar se o personagem chegou no alvo
        sound_effect = pygame.mixer.Sound("wavs/RUSH-E-_vocals_-_mp3cut.net_.wav")
        sound_effect.play()
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        state['is_moving'] = False
        state['tela_atual'] = 'fase2_instrucoes'


def fase1_instructions(window, assets, state): # Tela de instruções da fase 1
    pygame.mixer.music.load(assets['giorno'])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    img = pygame.image.load(assets['fase1_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: # Verifica se o jogador apertou a tecla espaço para ir para a fase 1
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'fase1'

def fase1_game(window, assets, state): # Tela da fase 1
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
    planeta = pygame.image.load(assets['planeta']).convert_alpha()
    planeta = pygame.transform.scale(planeta, (120, 120))
    window.blit(planeta, (state['planeta1_pos'][0], state['planeta1_pos'][1]))
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
            if event.button == 1 and not state['is_moving']: # Verifica se o personagem não está se movendo para que ele não possa ser lançado mais de uma vez
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
    if state['is_moving']: # Verifica se o personagem está se movendo para que ele possa ser atualizado
        update_state(state, assets)
