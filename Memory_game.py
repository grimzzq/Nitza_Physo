from CONSTANTS import *
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 50)
back_button = Button(50, HEIGHT - 150, 200, 50, "Exit", MENU)
color_keys = list(colors.keys())

def memory_game(current_state, running):
    sequence = []
    player_sequence = []
    waiting_for_input = False
    game_over = False

    def draw_rects(highlight=None):
        screen.blit(background_image, (0, 0))
        for color, rect in rects.items():
            base, bright = colors[color]
            pygame.draw.rect(screen, bright if color == highlight else base, rect)
        back_button.draw(screen)
        pygame.display.flip()

    def flash_sequence(seq):
        for color in seq:
            draw_rects(highlight=color)  # Highlight the current color
            pygame.time.delay(600)        # Hold color for 600 ms
            draw_rects()                  # Clear highlight
            pygame.time.delay(300)        # Delay before next flash

    def reset_game():
        nonlocal sequence, player_sequence, waiting_for_input, game_over
        sequence = []
        player_sequence = []
        game_over = False
        # Add a new random color to the sequence
        sequence.append(random.choice(color_keys))
        flash_sequence(sequence)  # Flash the initial sequence
        waiting_for_input = True   # Set to wait for input

    reset_game()

    while running:
        draw_rects()  # Draw the rectangles

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if back_button.check_click(event) == MENU:
                return MENU

            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_input and not game_over:
                for color, rect in rects.items():
                    if rect.collidepoint(event.pos):
                        player_sequence.append(color)  # Add clicked color to player's sequence
                        draw_rects(highlight=color)     # Highlight the clicked color
                        pygame.time.delay(300)          # Brief delay
                        draw_rects()                    # Clear highlight

                        # Check if the last player's input is correct
                        if player_sequence[-1] != sequence[len(player_sequence) - 1]:
                            game_over = True
                        elif len(player_sequence) == len(sequence):
                            pygame.time.delay(500)
                            sequence.append(random.choice(color_keys))
                            player_sequence = []
                            flash_sequence(sequence)

        if game_over:
            text = font.render("Game Over!", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            back_button.draw(screen)                 # Draw exit button
            pygame.display.flip()
            pygame.time.delay(1500)                  # Wait before resetting the game
            reset_game()                             # Reset the game after a delay

        pygame.display.flip()
        pygame.time.delay(20)



