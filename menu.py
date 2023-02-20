import pygame
from time import sleep

def main_menu(window: pygame.Surface, assets: dict, state: dict, clock: pygame.time.Clock, FPS):
    window.blit(pygame.image.load(assets['background']), (0, 0))
    sleep(5)
    window.blit(pygame.image.load(assets['menu1']), (0, 0))
    sleep(5)
    window.blit(pygame.image.load(assets['menu2']), (0, 0))
    sleep(5)
    window.blit(pygame.image.load(assets['menu3']), (0, 0))
    sleep(5)
    window.blit(pygame.image.load(assets['menu4']), (0, 0))
    sleep(5)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'fase1'
