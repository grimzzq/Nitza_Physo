from CONSTANTS import *

def credits_screen(current_state,running):
    while current_state == CREDITS:
        screen.blit(background_image, (0, 0))
        credits_text = font.render("Credits:", True, (255, 255, 255))
        names_text = font.render("N / O / S | Ashdod 3 Nitzanim ", True, (255, 255, 255))
        back_text = font.render("Click to go back", True, (255, 255, 255))

        screen.blit(credits_text, (WIDTH // 2 - credits_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(names_text, (WIDTH // 2 - names_text.get_width() // 2, HEIGHT // 2))
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                return MENU

def start_music():
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)