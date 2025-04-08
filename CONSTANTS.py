import pygame
from BUTTONS import Button
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Wellness Games')

background_image = pygame.image.load("the-majestic-antelope-canyon-pg-1920x1080.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

middle_image = pygame.image.load("Nitza.png")
middle_image = pygame.transform.scale(middle_image, (400, 400))

pygame.mixer.music.load("getaway.mp3")

font = pygame.font.Font(None, 60)

MENU = "menu"
BREATHING = "breathing"
HAND_TRACKING = "hand_tracking"
Memory = "Memory"
CREDITS = "credits"
GAMES_MENU = "games_menu"


button_width = 400
button_height = 80
button_spacing = 20
start_x = (WIDTH - button_width) // 2
start_y = (HEIGHT - (4 * button_height + 3 * button_spacing) - 250) // 2


Main_Menu = [
    Button(start_x, start_y + 2 *(button_height + button_spacing), button_width, button_height, "Credits", CREDITS),
    Button(start_x, start_y + 3 * (button_height + button_spacing), button_width, button_height, "Quit", "quit"),
    Button(start_x, start_y + (button_height + button_spacing), button_width, button_height,"Games", GAMES_MENU)
]

Games = [
    Button(start_x, start_y, button_width, button_height, "Breathing Exercise", BREATHING),
    Button(start_x , start_y + 2 * (button_height + button_spacing), button_width, button_height, "Memory game", Memory),
    Button(start_x, start_y + button_height + button_spacing, button_width, button_height, "Hand Tracking",HAND_TRACKING)

]

breath_instructions = ["Inhale...", "Hold...", "Exhale...", "Hold..."]
breath_durations = [4, 4, 6, 2]

colors = {
    "red": ((255, 0, 0), (150, 150, 150)),
    "purple": ((160, 32, 240), (150, 150, 150)),
    "blue": ((0, 0, 255), (150, 150, 150)),
    "black": ((0, 0, 0), (150, 150, 150))
}

rects = {
    "red": pygame.Rect((WIDTH - 150) // 2 - 80, (HEIGHT - 150) // 2 - 80, 150, 150),
    "green": pygame.Rect((WIDTH - 150) // 2 + 80, (HEIGHT - 150) // 2 - 80, 150, 150),
    "blue": pygame.Rect((WIDTH - 150) // 2 - 80, (HEIGHT - 150) // 2 + 80, 150, 150),
    "yellow": pygame.Rect((WIDTH - 150) // 2 + 80, (HEIGHT - 150) // 2 + 80, 150, 150)
}
