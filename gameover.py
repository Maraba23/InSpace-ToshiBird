import pygame

def play_music(assets):
    pygame.mixer.music.load(assets['gameover_song'])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def game_over_screen(window, state, assets):
    play_music(assets=assets)
    img = pygame.image.load(assets['gameover']).convert()
    img = pygame.transform.scale(img, (1280, 720))
    window.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state['tela_atual'] = 'menu'
