import pygame
from pygame_m.scenes.base_scene import BaseScene
from pygame_m.components.ui_button import UIButton
from pygame_m.components.ui_label import UILabel
from pygame_m.config import settings

class InteractionScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.counter = 0
        self.label = UILabel(settings.WINDOW_WIDTH//2 - 50, 200, f"Valor: {self.counter}", 64)
        
        self.buttons = [
            UIButton(settings.WINDOW_WIDTH//2 - 220, 320, 140, 50, "+ Incrementar", self._increment),
            UIButton(settings.WINDOW_WIDTH//2 + 80, 320, 140, 50, "- Decrementar", self._decrement),
            UIButton(settings.WINDOW_WIDTH//2 - 100, 420, 200, 50, "Guardar y Continuar", self._go_to_result)
        ]

    def _increment(self):
        self.counter += 1
        self.label.update_text(f"Valor: {self.counter}")

    def _decrement(self):
        if self.counter > 0:
            self.counter -= 1
            self.label.update_text(f"Valor: {self.counter}")

    def _go_to_result(self):
        from pygame_m.scenes.result_scene import ResultScene
        # Pasamos el estado (counter) a la siguiente escena
        self.game.change_scene(ResultScene(self.game, self.counter))

    def handle_event(self, event: pygame.event.Event) -> None:
        for btn in self.buttons:
            btn.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from pygame_m.scenes.menu_scene import MenuScene
            self.game.change_scene(MenuScene(self.game))

    def update(self, delta_time: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(settings.BACKGROUND_COLOR)
        self.label.draw(surface)
        for btn in self.buttons:
            btn.draw(surface)