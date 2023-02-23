import pygame

def main_menu(window: pygame.Surface, assets: dict, state: dict):
    menu = pygame.image.load(assets['menu4']).convert_alpha()
    menu = pygame.transform.scale(menu, (1280, 720))
    window.blit(menu, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'story'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def story_screen(window: pygame.Surface, assets: dict, state: dict):
    story = pygame.image.load(assets['story']).convert_alpha()
    story = pygame.transform.scale(story, (1280, 720))
    window.blit(story, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'instructions'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def instructions_screen(window: pygame.Surface, assets: dict, state: dict):
    instructinos = pygame.image.load(assets['instructions']).convert_alpha()
    instructinos = pygame.transform.scale(instructinos, (1280, 720))
    window.blit(instructinos, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'fase1_instrucoes'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
