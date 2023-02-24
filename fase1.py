import pygame
import random
import math

G_CONST = 10

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def target_reached(state):
    target_rect = pygame.Rect(state['target_pos'][0][0], state['target_pos'][0][1], state['target_pos'][1][0] - state['target_pos'][0][0], state['target_pos'][1][1] - state['target_pos'][0][1])
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(target_rect)

def collision_planeta(state):
    planeta_rect = pygame.Rect(state['planeta1_pos'][0], state['planeta1_pos'][1], 120, 120)
    char_rect = pygame.Rect(state['char_pos'][0], state['char_pos'][1], 75, 75)
    return char_rect.colliderect(planeta_rect)

def out_of_bounds(state):
    return state['char_pos'][0] < 0 or state['char_pos'][0] > 1280 or state['char_pos'][1] < 0 or state['char_pos'][1] > 860

def update_state(state, assets):
    f_grav = (G_CONST * state['char_mass'] * state['planeta1_mass']) / (dist(state['char_pos'], state['planeta1_pos']) ** 2)
    # get the angle between the character and the center of the planet
    angle_p = math.atan2(state['planeta1_pos'][1] - state['char_pos'][1], state['planeta1_pos'][0] - state['char_pos'][0])
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
        state['tela_atual'] = 'fase1'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0:
            state['tela_atual'] = 'game_over'
    elif out_of_bounds(state):
        state['is_moving'] = False
        state['tela_atual'] = 'fase1'
        state['vidas'] -= 1
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        if state['vidas'] == 0:
            state['tela_atual'] = 'game_over'
    elif target_reached(state):
        state['char_pos'] = (int(75/2), int(assets['height']/2))
        state['is_moving'] = False
        state['tela_atual'] = 'fase2_instrucoes'

def fase1_instructions(window, assets, state):
    img = pygame.image.load(assets['fase1_instrucoes']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'fase1'

def fase1_game(window, assets, state):
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
            if event.key == pygame.K_RETURN:
                state['tela_atual'] = 'menu'
                state['vidas'] = 3
                state['char_pos'] = (int(75/2), int(assets['height']/2))
                state['is_moving'] = False
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
