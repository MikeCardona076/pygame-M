# Arquitectura de pygame-M

La estructura separa el arranque del juego, el ciclo principal, la configuración
y las escenas. La primera escena implementada es una pantalla de bienvenida.

## Estructura actual

```text
src/pygame_m/
├── __init__.py
├── __main__.py
├── app.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── core/
│   ├── __init__.py
│   └── game.py
└── scenes/
    ├── __init__.py
    ├── base_scene.py
    └── welcome_scene.py
```

## Responsabilidades

- **`__main__.py`**: permite iniciar el paquete con `python -m pygame_m`.
- **`app.py`**: crea y ejecuta la instancia del juego.
- **`config/settings.py`**: concentra el tamaño de ventana, el límite de FPS y
  los colores de la interfaz.
- **`core/game.py`**: inicializa Pygame, procesa eventos y coordina la escena
  activa en cada iteración del ciclo principal.
- **`scenes/base_scene.py`**: define el contrato común de una escena.
- **`scenes/welcome_scene.py`**: dibuja la pantalla de bienvenida y responde a
  Escape.

## Flujo

`__main__` llama a `app`, que crea el juego. El ciclo principal entrega los
eventos y la superficie de dibujo a la escena activa; la escena actualiza su
estado y dibuja un fotograma. Cerrar la ventana o pulsar Escape termina el ciclo
y libera los recursos de Pygame.

Las entidades, sistemas, recursos externos y escenas adicionales se agregarán
cuando haya una funcionalidad que los necesite. Así la base se mantiene simple y
las dependencias apuntan desde el arranque hacia los módulos de juego, no al
revés.
