import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 0, 0)
        self.hover_color = (255, 255, 255)

    def draw(self, screen, hover=False):
        font = pygame.font.Font(None, 60)
        color = self.hover_color if hover else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)

        text_surface = font.render(self.text, True, (0, 0, 0) if hover else (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                    self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.action
        return None