import pygame

def fase1_game(window, assets, state, clock, FPS):
    window.blit(pygame.image.load(assets['background']), (0, 0))
    sleep(1)
    window.blit(pygame.image.load(assets['menu4']), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'story'
                return state