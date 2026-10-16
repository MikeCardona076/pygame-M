"""Componente de botón reutilizable con estados visuales."""
import pygame
from pygame_m.config import settings

class UIButton:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, action_callback: callable):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action_callback = action_callback
        
        # Estilos elegantes y sutiles
        self.color_normal = (51, 65, 85)      # Slate-700
        self.color_hover = (71, 85, 105)      # Slate-600
        self.color_active = (30, 41, 59)      # Slate-800
        self.text_color = (245, 247, 255)     # Slate-50
        
        self.font = pygame.font.Font(None, 36)
        self.is_hovered = False

    def handle_event(self, event: pygame.event.Event) -> bool:
        """Procesa eventos del ratón. Retorna True si se hizo clic."""
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                self.action_callback()
                return True
        return False

    def draw(self, surface: pygame.Surface) -> None:
        color = self.color_hover if self.is_hovered else self.color_normal
        # Dibujar fondo con bordes redondeados (simulado con rect o nativo en pygame 2+)
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        
        # Renderizar texto centrado
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)