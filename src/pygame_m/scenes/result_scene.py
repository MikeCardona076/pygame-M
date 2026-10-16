from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from pygame_m.components.ui_button import UIButton
from pygame_m.config import settings
from pygame_m.scenes.base_scene import BaseScene

if TYPE_CHECKING:
    from pygame_m.core.game import Game


class ResultScene(BaseScene):
    def __init__(self, game: Game, final_value: int) -> None:
        super().__init__(game)
        self.final_value = final_value
        self.title_font = pygame.font.Font(None, 64)
        self.info_font = pygame.font.Font(None, 48)
        self.buttons = [
            UIButton(
                settings.WINDOW_WIDTH // 2 - 100,
                350,
                200,
                50,
                "Volver al Inicio",
                self._go_to_menu,
            )
        ]

    def _go_to_menu(self) -> None:
        from pygame_m.scenes.menu_scene import MenuScene

        self.game.change_scene(MenuScene(self.game))

    def handle_event(self, event: pygame.event.Event) -> None:
        for btn in self.buttons:
            btn.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._go_to_menu()

    def update(self, _delta_time: float) -> None:
        del _delta_time

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(settings.BACKGROUND_COLOR)

        title = self.title_font.render(
            "¡Proceso Completado!", True, (16, 185, 129)
        )
        surface.blit(
            title,
            title.get_rect(center=(settings.WINDOW_WIDTH // 2, 150)),
        )

        info = self.info_font.render(
            f"Valor final guardado: {self.final_value}",
            True,
            settings.PRIMARY_TEXT_COLOR,
        )
        surface.blit(
            info,
            info.get_rect(center=(settings.WINDOW_WIDTH // 2, 250)),
        )

        for btn in self.buttons:
            btn.draw(surface)