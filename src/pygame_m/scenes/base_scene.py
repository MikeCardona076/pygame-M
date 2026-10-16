"""Contrato para las escenas del juego."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from pygame_m.core.game import Game


class BaseScene(ABC):
    def __init__(self, game: Game | None = None) -> None:
        self.game = game

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Procesa un evento de Pygame."""

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Actualiza la escena usando el tiempo transcurrido en segundos."""

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        """Dibuja la escena sobre la superficie recibida."""
