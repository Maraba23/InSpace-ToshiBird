import pygame
import random
import math
from fase1 import dist, target_reached, out_of_bounds

G_CONST = 10

def collision_planeta(state): # Função que verifica se o personagem colidiu com o planeta
    planeta1_rect = pygame.Rect(state['planeta3_pos'][0][0], state['planeta3_pos'][0][1], 120, 120)
    planeta2_rect = pygame.Rect(state['planeta3_pos'][1][0], state['planeta3_pos'][1][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta1_rect) or char_rect.colliderect(planeta2_rect)

def update_state(state, assets): # Função que atualiza o estado do jogo
    # calculate the forces between the character and the planets
    f_grav = (G_CONST * state['char_mass'] * state['planeta2_mass']) / (dist(state['char_pos'], state['planeta3_pos'][0]) ** 2)
    f_grav_2 = (G_CONST * state['char_mass'] * state['planeta1_mass']) / (dist(state['char_pos'], state['planeta3_pos'][1]) ** 2)
    # get the angle between the character and the center of the planet
    angle_p = math.atan2(state['planeta3_pos'][0][1] - state['char_pos'][1], state['planeta3_pos'][0][0] - state['char_pos'][0])
    angle_p_2 = math.atan2(state['planeta3_pos'][1][1] - state['char_pos'][1], state['planeta3_pos'][1][0] - state['char_pos'][0])
    # calculate the x and y components of the force
    f_x = f_grav * math.cos(angle_p)
    f_y = f_grav * math.sin(angle_p)
    f_x_2 = f_grav_2 * math.cos(angle_p_2)
    f_y_2 = f_grav_2 * math.sin(angle_p_2)
    # calculate the acceleration
    a_x = f_x / state['char_mass']
    a_y = f_y / state['char_mass']
    a_x_2 = f_x_2 / state['char_mass']
    a_y_2 = f_y_2 / state['char_mass']
    state['char_acc'] = [a_x + a_x_2, a_y + a_y_2]
    # update the velocity
    state['char_vel'] = (state['char_vel'][0] + state['char_acc'][0], state['char_vel'][1] + state['char_acc'][1])
    # update the position
    state['char_pos'] = (state['char_pos'][0] + state['char_vel'][0], state['char_pos'][1] + state['char_vel'][1])
    if collision_planeta(state): # Se o personagem colidir com o planeta, ele volta para a posição inicial e perde uma vida
        state['is_moving'] = False
        state['tela_atual'] = 'fase3'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0: # Se o personagem perder todas as vidas, ele vai para a tela de game over
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif out_of_bounds(state): # Se o personagem sair da tela, ele volta para a posição inicial e perde uma vida
        state['is_moving'] = False
        state['tela_atual'] = 'fase3'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0: # Se o personagem perder todas as vidas, ele vai para a tela de game over
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif target_reached(state): # Se o personagem chegar no alvo, ele vai para a tela de vitória
        sound_effect = pygame.mixer.Sound("wavs/RUSH-E-_vocals_-_mp3cut.net_.wav")
        sound_effect.play()
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        state['is_moving'] = False
        state['tela_atual'] = 'fase4_instrucoes'

def fase3_instructions(window, assets, state): # Tela de instruções da fase 3
    img = pygame.image.load(assets['fase3_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Se o jogador apertar espaço, ele vai para a fase 3
                state['tela_atual'] = 'fase3'

def fase3_game(window, assets, state): # Tela da fase 3
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
    planeta1 = pygame.image.load(assets['planeta']).convert_alpha()
    planeta1 = pygame.transform.scale(planeta1, (100, 100))
    window.blit(planeta1, (state['planeta3_pos'][0][0], state['planeta3_pos'][0][1]))
    planeta2 = pygame.image.load(assets['planeta']).convert_alpha()
    planeta2 = pygame.transform.scale(planeta2, (120, 120))
    window.blit(planeta2, (state['planeta2_pos'][0], state['planeta2_pos'][1]))
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
            if event.button == 1 and not state['is_moving']: # Se o personagem não estiver se movendo, ele vai para a posição do mouse
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
    if state['is_moving']: # Se o personagem estiver se movendo, ele vai para a posição do mouse
        update_state(state, assets)