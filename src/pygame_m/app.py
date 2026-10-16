import argparse
from collections.abc import Sequence

from pygame_m import __version__


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m pygame_m",
        description="Inicia pygame-M y muestra su pantalla de bienvenida.",
        epilog=(
            "Comandos basicos:\n"
            "  python -m pygame_m          Iniciar la pantalla de bienvenida\n"
            "  python -m pygame_m --help   Mostrar esta ayuda\n"
            "  python -m pygame_m --version Mostrar la version instalada"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"pygame-m {__version__}",
        help="mostrar la version instalada",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    create_parser().parse_args(argv)

    from pygame_m.core.game import Game
    from pygame_m.scenes.welcome_scene import WelcomeScene

    game = Game(WelcomeScene)
    game.run()
