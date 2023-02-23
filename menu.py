import pygame

def main_menu(window: pygame.Surface, assets: dict, state: dict):
    window.blit(pygame.image.load(assets['menu4']), (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'story'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def story_screen(window: pygame.Surface, assets: dict, state: dict):
    window.blit(pygame.image.load(assets['story']), (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'instructions'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()

def instructions_screen(window: pygame.Surface, assets: dict, state: dict):
    window.blit(pygame.image.load(assets['instructions']), (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'fase1_instrucoes'
            pygame.mixer.music.play()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
