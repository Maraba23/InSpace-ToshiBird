import pygame
import random
import math
from fase1 import dist, target_reached, out_of_bounds

G_CONST = 10

def collision_planeta(state):
    planeta1_rect = pygame.Rect(state['planeta4_pos'][0][0], state['planeta4_pos'][0][1], 120, 120)
    planeta2_rect = pygame.Rect(state['planeta4_pos'][1][0], state['planeta4_pos'][1][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta1_rect) or char_rect.colliderect(planeta2_rect)

def desafio_instructions(window, assets, state):
    img = pygame.image.load(assets['desafio_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("musicas/Dark souls.mp3")
                pygame.mixer.music.play(-1)
                state['tela_atual'] = 'desafio'
            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
                sound_effect.play()
                state['tela_atual'] = 'win_no_challenge'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False

def update_state(state, assets):
    f_grav = (G_CONST * state['char_mass'] * state['planeta1_mass']) / (dist(state['char_pos'], state['planeta4_pos'][0]) ** 2)
    f_grav2 = (G_CONST * state['char_mass'] * state['planeta1_mass']) / (dist(state['char_pos'], state['planeta4_pos'][1]) ** 2)
    # get the angle between the character and the center of the planet
    angle_p = math.atan2(state['planeta4_pos'][0][1] - state['char_pos'][1], state['planeta4_pos'][0][0] - state['char_pos'][0])
    angle_p2 = math.atan2(state['planeta4_pos'][1][1] - state['char_pos'][1], state['planeta4_pos'][1][0] - state['char_pos'][0])
    # calculate the force vector
    f_x = f_grav * math.cos(angle_p)
    f_y = f_grav * math.sin(angle_p)
    f_x2 = f_grav2 * math.cos(angle_p2)
    f_y2 = f_grav2 * math.sin(angle_p2)
    # calculate the acceleration
    a_x = f_x / state['char_mass']
    a_y = f_y / state['char_mass']
    a_x2 = f_x2 / state['char_mass']
    a_y2 = f_y2 / state['char_mass']
    # update the acceleration
    state['char_acc'] = (a_x + a_x2, a_y + a_y2)
    # update the velocity
    state['char_vel'] = (state['char_vel'][0] + state['char_acc'][0], state['char_vel'][1] + state['char_acc'][1])
    # update the position
    state['char_pos'] = (state['char_pos'][0] + state['char_vel'][0], state['char_pos'][1] + state['char_vel'][1])
    # check if the character reached the target
    if target_reached(state):
        pygame.mixer.music.stop()
        sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
        sound_effect.play()
        state['tela_atual'] = 'win_challenge'
    # check if the character is out of bounds
    if out_of_bounds(state):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(assets['gameover_song'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        state['tela_atual'] = 'game_over'
    # check if the character collided with the planet
    if collision_planeta(state):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(assets['gameover_song'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        state['tela_atual'] = 'game_over'

def desafio_game(window, assets, state):
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
            if event.key == pygame.K_RETURN:
                state['tela_atual'] = 'menu'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
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


