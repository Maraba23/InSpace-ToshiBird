import pygame
import random
import math
from fase1 import dist, target_reached, out_of_bounds

G_CONST = 10

def collision_planeta(state):
    planeta_rect = pygame.Rect(state['buraco_negro_pos'][0], state['buraco_negro_pos'][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta_rect)

def update_state(state, assets):
    f_grav = (G_CONST * state['char_mass'] * state['buraco_negro_mass']) / (dist(state['char_pos'], state['buraco_negro_pos']) ** 2)
    # get the angle between the character and the center of the planet
    angle_p = math.atan2(state['buraco_negro_pos'][1] - state['char_pos'][1], state['buraco_negro_pos'][0] - state['char_pos'][0])
    # calculate the acceleration vector
    acc_x = f_grav * math.cos(angle_p)
    acc_y = f_grav * math.sin(angle_p)
    # update the character acceleration
    state['char_acc'] = (acc_x, acc_y)
    # update the character position
    state['char_pos'] = (state['char_pos'][0] + state['char_vel'][0], state['char_pos'][1] + state['char_vel'][1])
    # update the character velocity
    state['char_vel'] = (state['char_vel'][0] + state['char_acc'][0], state['char_vel'][1] + state['char_acc'][1])
    if collision_planeta(state):
        state['is_moving'] = False
        state['tela_atual'] = 'fase4'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0:
            state['tela_atual'] = 'game_over'
    elif out_of_bounds(state):
        state['is_moving'] = False
        state['tela_atual'] = 'fase4'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(assets['gameover_song'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            state['tela_atual'] = 'game_over'
    elif target_reached(state):
        sound_effect = pygame.mixer.Sound("wavs/Happy-Wheels.wav")
        sound_effect.play()
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        state['is_moving'] = False
        state['tela_atual'] = 'fase5_instrucoes'
        state['vidas'] = 5

def fase4_instructions(window, assets, state):
    img = pygame.image.load(assets['fase4_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'fase4'

def fase4_game(window, assets, state):
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
            if event.key == pygame.K_RETURN:
                state['vidas'] = 3
                state['tela_atual'] = 'menu'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not state['is_moving']:
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