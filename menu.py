import pygame

def main_menu(window: pygame.Surface, assets: dict, state: dict, clock, FPS):
    window.blit(pygame.image.load(assets['menu4']), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            state['tela_atual'] = 'story'
            return state

def story_screen(window: pygame.Surface, assets: dict, state: dict, clock, FPS):
    window.blit(pygame.image.load(assets['story']), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'instructions'
                return state

def instructions_screen(window: pygame.Surface, assets: dict, state: dict, clock, FPS):
    window.blit(pygame.image.load(assets['instructions']), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'fase1'
                return state