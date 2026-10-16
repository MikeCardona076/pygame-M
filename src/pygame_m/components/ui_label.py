"""Componente de etiqueta de texto estático."""
import pygame

class UILabel:
    def __init__(self, x: int, y: int, text: str, font_size: int = 48, color: tuple = (245, 247, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, font_size)

    def update_text(self, new_text: str) -> None:
        self.text = new_text

    def draw(self, surface: pygame.Surface) -> None:
        text_surf = self.font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(topleft=(self.x, self.y))
        surface.blit(text_surf, text_rect)