import pygame
from pygame_m.scenes.base_scene import BaseScene
from pygame_m.components.ui_button import UIButton
from pygame_m.config import settings

class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.buttons = [
            UIButton(settings.WINDOW_WIDTH//2 - 100, 300, 200, 50, "Iniciar App", self._go_to_interaction),
            UIButton(settings.WINDOW_WIDTH//2 - 100, 380, 200, 50, "Salir", self._quit_game)
        ]

    def _go_to_interaction(self):
        from pygame_m.scenes.interaction_scene import InteractionScene
        self.game.change_scene(InteractionScene(self.game))

    def _quit_game(self):
        self.game.running = False

    def handle_event(self, event: pygame.event.Event) -> None:
        for btn in self.buttons:
            btn.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.running = False

    def update(self, delta_time: float) -> None:
        pass # Lógica estática

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(settings.BACKGROUND_COLOR)
        title_font = pygame.font.Font(None, 72)
        title = title_font.render("Mini App UI", True, settings.ACCENT_COLOR)
        surface.blit(title, title.get_rect(center=(settings.WINDOW_WIDTH//2, 150)))
        
        for btn in self.buttons:
            btn.draw(surface)