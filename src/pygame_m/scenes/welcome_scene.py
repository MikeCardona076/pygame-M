"""Pantalla inicial de pygame-M."""

import pygame

from pygame_m.config import settings
from pygame_m.scenes.base_scene import BaseScene


class WelcomeScene(BaseScene):
    def __init__(self) -> None:
        self.title_font = pygame.font.Font(None, 88)
        self.subtitle_font = pygame.font.Font(None, 32)
        self.hint_font = pygame.font.Font(None, 24)

    def handle_event(self, _event: pygame.event.Event) -> None:
        del _event

    def update(self, _delta_time: float) -> None:
        del _delta_time

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(settings.BACKGROUND_COLOR)

        center_x = settings.WINDOW_WIDTH // 2
        pygame.draw.circle(surface, settings.ACCENT_COLOR, (center_x, 155), 5)
        pygame.draw.line(
            surface,
            (39, 53, 81),
            (center_x - 180, 180),
            (center_x + 180, 180),
            2,
        )

        title = self.title_font.render("Pygame-M", True, settings.PRIMARY_TEXT_COLOR)
        subtitle = self.subtitle_font.render(
            "Tu punto de partida para crear juegos",
            True,
            settings.SECONDARY_TEXT_COLOR,
        )
        hint = self.hint_font.render(
            "Presiona ESC para salir",
            True,
            settings.SECONDARY_TEXT_COLOR,
        )

        surface.blit(title, title.get_rect(center=(center_x, 250)))
        surface.blit(subtitle, subtitle.get_rect(center=(center_x, 320)))
        surface.blit(hint, hint.get_rect(center=(center_x, 475)))

        pygame.draw.line(
            surface,
            settings.ACCENT_COLOR,
            (center_x - 42, 375),
            (center_x + 42, 375),
            3,
        )
