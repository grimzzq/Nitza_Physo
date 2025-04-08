import sys

import CONSTANTS
from Hand_Tracking import *
from Breath_excersise import *
from Extras import *
from Memory_game import *
from CONSTANTS import *  # Import all constants from your constants file

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Wellness Games')

# Start music
start_music()

current_state = MENU
running = True

while running:
    screen.blit(background_image, (0, 0))  # Draw background

    if current_state == MENU:
        # Draw the main menu buttons
        for button in Main_Menu:
            button.draw(screen, hover=button.rect.collidepoint(pygame.mouse.get_pos()))

        middle_image_rect = middle_image.get_rect(center=(WIDTH // 2, start_y + 4 * (button_height + button_spacing) + 100))
        screen.blit(middle_image, middle_image_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in Main_Menu + [CONSTANTS.Main_Menu[2]]:
                action = button.check_click(event)
                if action:
                    if action == "quit":
                        running = False
                    else:
                        current_state = action

    elif current_state == GAMES_MENU:
        # Draw buttons for each game
        for button in Games:
            button.draw(screen, hover=button.rect.collidepoint(pygame.mouse.get_pos()))

        # Back button to return to the main menu
        back_button = Button(start_x, HEIGHT - 150, button_width, button_height, "Back", MENU)
        back_button.draw(screen, hover=back_button.rect.collidepoint(pygame.mouse.get_pos()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in Games + [back_button]:
                action = button.check_click(event)
                if action:
                    if action == MENU:
                        current_state = MENU
                    else:
                        current_state = action

    elif current_state == BREATHING:
        if breathing_exercise(current_state, running) == MENU:
            current_state = MENU
    elif current_state == HAND_TRACKING:
        if hand_tracking_game(current_state, running) == MENU:
            current_state = MENU
    elif current_state == CREDITS:
        if credits_screen(current_state, running) == MENU:
            current_state = MENU
    elif current_state == Memory:
        if memory_game(current_state, running) == MENU:
            current_state = MENU

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()