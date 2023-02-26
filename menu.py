import pygame

def main_menu(window: pygame.Surface, assets: dict, state: dict): # Menu principal do jogo (tela inicial)
    menu = pygame.image.load(assets['menu4']).convert_alpha()
    menu = pygame.transform.scale(menu, (1280, 720))
    window.blit(menu, (0, 0))
    for event in pygame.event.get(): 
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): # Se o jogador apertar espaço, a tela atual do jogo muda para a tela de história
            state['tela_atual'] = 'story'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def story_screen(window: pygame.Surface, assets: dict, state: dict): # Tela de história do jogo
    story = pygame.image.load(assets['story']).convert_alpha()
    story = pygame.transform.scale(story, (1280, 720))
    window.blit(story, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): # Se o jogador apertar espaço, a tela atual do jogo muda para a tela de instruções
            state['tela_atual'] = 'instructions'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def instructions_screen(window: pygame.Surface, assets: dict, state: dict): # Tela de instruções do jogo
    instructinos = pygame.image.load(assets['instructions']).convert_alpha()
    instructinos = pygame.transform.scale(instructinos, (1280, 720))
    window.blit(instructinos, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): # Se o jogador apertar espaço, a tela atual do jogo muda para a tela de instruções da fase 1
            state['tela_atual'] = 'fase1_instrucoes'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def win_screen_no_challenges(window, assets, state): # Tela de vitória sem desafios (caso o jogador não feito a fase de desafio)
    win_no = pygame.image.load(assets['win_no_challenge']).convert_alpha()
    win_no = pygame.transform.scale(win_no, (1280, 720))
    window.blit(win_no, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): # Se o jogador apertar espaço, a tela atual do jogo muda para a tela de menu principal e as vidas do jogador voltam a ser 3
            pygame.mixer.music.load(assets['e_sound'])
            pygame.mixer.music.set_volume(0.5)
            state['tela_atual'] = 'menu'
            state['vidas'] = 3
            state['char_pos'] = (int(75/2), int(assets['height']/2))
            state['is_moving'] = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def win_screen_challenges(window, assets, state): # Tela de vitória com desafios (caso o jogador feito a fase de desafio)
    win_ch = pygame.image.load(assets['win_challenge']).convert_alpha()
    win_ch = pygame.transform.scale(win_ch, (1280, 720))
    window.blit(win_ch, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE): # Se o jogador apertar espaço, a tela atual do jogo muda para a tela de menu principal e as vidas do jogador voltam a ser 3
            pygame.mixer.music.load(assets['e_sound'])
            pygame.mixer.music.set_volume(0.5)
            state['tela_atual'] = 'menu'
            state['vidas'] = 3
            state['char_pos'] = (int(75/2), int(assets['height']/2))
            state['is_moving'] = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

