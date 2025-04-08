from CONSTANTS import *
import time
import math

def draw_waves(t, amp, freq):
    points = []
    for x in range(0, WIDTH, 5):
        y = int(HEIGHT // 2 + amp * math.sin((x * freq) + t))
        points.append((x, y))
    pygame.draw.lines(screen, (173, 216, 230), False, points, 2)

def breathing_exercise(current_state, running):
    back_button = Button(50, HEIGHT - 150, 200, 50, "Exit", MENU)
    while running:
        for i, instruction in enumerate(breath_instructions):
            start_time = time.time()
            while time.time() - start_time < breath_durations[i]:
                elapsed = time.time() - start_time
                screen.blit(background_image, (0, 0))

                if i == 0:
                    amp = 50 + (elapsed / breath_durations[i]) * 100
                    freq = 0.02
                    draw_waves(elapsed * 2 * math.pi, amp, freq)
                elif i == 1:
                    amp = 100
                    freq = 0.02
                    draw_waves(breath_durations[i], amp, freq)
                elif i == 2:
                    amp = 100 - (elapsed / breath_durations[i]) * 100
                    freq = 0.02
                    draw_waves(elapsed * 2 * math.pi, amp, freq)
                else:
                    amp = 0
                    freq = 0.02
                    draw_waves(breath_durations[i], amp, freq)

                text_surface = font.render(instruction, True, (255, 255, 255))
                screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - 50))
                back_button.draw(screen)

                pygame.display.flip()
                pygame.time.delay(20)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        return
                    if back_button.check_click(event) == MENU:
                        return MENU

        continue_exercise = False
        while not continue_exercise:
            screen.blit(background_image, (0, 0))
            continue_text = font.render("Continue breathing exercise? (Y/N)", True, (255, 255, 255))
            screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2 - 50))
            back_button.draw(screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        continue_exercise = True
                    elif event.key == pygame.K_n:
                        return MENU
                if back_button.check_click(event) == MENU:
                    return MENU

    return MENU