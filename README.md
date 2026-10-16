# pygame-M

Proyecto educativo para aprender a estructurar juegos con
[Pygame](https://www.pygame.org/). Usa Pygame Community Edition, compatible con
la API `pygame` y con Python 3.14.

## Estado

La estructura inicial ya es ejecutable. Al iniciarlo se abre una ventana de
bienvenida con el texto **Pygame-M**. El proyecto todavía no incluye niveles,
jugador ni mecánicas de juego.

## Estructura

```text
pygame-M/
├── docs/
│   └── arquitectura.md
├── src/
│   └── pygame_m/
│       ├── config/settings.py
│       ├── core/game.py
│       ├── scenes/base_scene.py
│       ├── scenes/welcome_scene.py
│       └── __main__.py
├── tests/
│   └── test_welcome_scene.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Requisitos

- Python 3.10 o superior
- pip

## Instalación y ejecución

Desde la carpeta del proyecto, crea y activa un entorno virtual.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux o macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala el proyecto y su dependencia, y ejecuta la pantalla inicial:

```bash
python -m pip install -e .
python -m pygame_m
```

Cierra la ventana o presiona **Esc** para salir.

## Comandos básicos

```bash
python -m pygame_m          # Iniciar la pantalla de bienvenida
python -m pygame_m --help   # Ver los comandos disponibles
python -m pygame_m --version
```

## Pruebas

```bash
python -m unittest discover -s tests
```

## Próximos pasos

1. Añadir movimiento del jugador y manejo de entrada.
2. Crear escenas de menú y juego.
3. Incorporar recursos y ejemplos cuando sean necesarios.

La arquitectura y las responsabilidades de cada módulo están explicadas en
[docs/arquitectura.md](docs/arquitectura.md).
