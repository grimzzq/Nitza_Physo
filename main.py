import sys
from Hand_Tracking import *
from Breath_excersise import *
from Extras import *
from Memory_game import *
current_state = MENU
running = True
start_music()

while running:
    screen.blit(background_image, (0, 0))
    if current_state == MENU:
        for button in buttons:
            button.draw(screen, hover=button.rect.collidepoint(pygame.mouse.get_pos()))
        middle_image_rect = middle_image.get_rect(center=(WIDTH // 2, start_y + 5* (button_height + button_spacing) + 100))
        screen.blit(middle_image, middle_image_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                action = button.check_click(event)
                if action:
                    if action == "quit":
                        running = False
                    else:
                        current_state = action

    elif current_state == BREATHING:
        if breathing_exercise(current_state, running) == MENU:
            current_state = MENU
    elif current_state == HAND_TRACKING:
        if hand_tracking_game(current_state, running) == MENU:
            current_state = MENU
    elif current_state == CREDITS:
        if credits_screen(current_state,running) == MENU:
            current_state = MENU
    elif current_state == Memory:
        if memory_game(current_state,running) == MENU:
            current_state = MENU

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
