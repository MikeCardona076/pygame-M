"""Ciclo principal y coordinación de escenas."""

from collections.abc import Callable

import pygame

from pygame_m.config import settings
from pygame_m.scenes.base_scene import BaseScene


class Game:
    def __init__(self, initial_scene: Callable[[], BaseScene]) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(settings.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.scene = initial_scene()
        self.running = True

    def run(self) -> None:
        try:
            while self.running:
                delta_time = self.clock.tick(settings.TARGET_FPS) / 1000
                self._handle_events()
                if self.running:
                    self.scene.update(delta_time)
                    self.scene.draw(self.screen)
                    pygame.display.flip()
        finally:
            pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False
            else:
                self.scene.handle_event(event)
