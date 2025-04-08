import random
from CONSTANTS import *
import time
import pygame

class MovingDot:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.target_x = self.x
        self.target_y = self.y
        self.radius = 30
        self.color = (255, 223, 0)
        self.speed = 0.1

    def move(self):
        self.target_x = random.randint(50, WIDTH - 50)
        self.target_y = random.randint(50, HEIGHT - 50)

    def update_position(self):
        self.x += (self.target_x - self.x) * self.speed
        self.y += (self.target_y - self.y) * self.speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def hand_tracking_game(current_state, running):
    dot = MovingDot()

    back_button = Button(50, HEIGHT - 150, 200, 50, "Exit", MENU)

    def increase_speed():
        dot.speed += 1

    speed_button = Button(1000, HEIGHT - 155, 250, 50, "Speed up", increase_speed)

    start_time = time.time()
    while time.time() - start_time < 15:
        screen.blit(background_image, (0, 0))
        dot.update_position()
        dot.draw()
        back_button.draw(screen)
        speed_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

            if event.type == pygame.MOUSEMOTION:
                if ((event.pos[0] - dot.x) ** 2 + (event.pos[1] - dot.y) ** 2) ** 0.5 < dot.radius:
                    dot.move()
                    start_time = time.time()

            if back_button.check_click(event):
                return MENU

            speed_button.check_click(event)

        pygame.display.flip()
        pygame.time.delay(50)

    return MENU

