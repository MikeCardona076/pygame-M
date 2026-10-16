"""Contrato para las escenas del juego."""

from abc import ABC, abstractmethod

import pygame


class BaseScene(ABC):
    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Procesa un evento de Pygame."""

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Actualiza la escena usando el tiempo transcurrido en segundos."""

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        """Dibuja la escena sobre la superficie recibida."""
