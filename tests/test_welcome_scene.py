import os
import unittest
from unittest.mock import Mock

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame

from pygame_m.core.game import Game
from pygame_m.scenes.welcome_scene import WelcomeScene


class WelcomeSceneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pygame.init()
        pygame.display.set_mode((1, 1))

    @classmethod
    def tearDownClass(cls) -> None:
        pygame.quit()

    def test_draws_without_error(self) -> None:
        scene = WelcomeScene()
        scene.title_font = Mock()
        scene.title_font.render.return_value = pygame.Surface((200, 80))
        surface = pygame.Surface((960, 540))

        scene.draw(surface)

        self.assertEqual(surface.get_at((0, 0))[:3], (13, 18, 35))
        scene.title_font.render.assert_called_once()
        self.assertEqual(scene.title_font.render.call_args.args[0], "Pygame-M")

    def test_escape_stops_the_game(self) -> None:
        game = Game(WelcomeScene)
        pygame.event.clear()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))

        game._handle_events()

        self.assertFalse(game.running)


if __name__ == "__main__":
    unittest.main()
