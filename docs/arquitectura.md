# Arquitectura de pygame-M

La estructura separa el arranque del juego, el ciclo principal, la configuración
y las escenas. El ejemplo incluye un menú, una escena de interacción con un
contador y una escena de resultado.

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
├── scenes/
│   ├── __init__.py
│   ├── base_scene.py
│   ├── welcome_scene.py
│   ├── menu_scene.py
│   ├── interaction_scene.py
│   └── result_scene.py
└── components/
    ├── ui_button.py
    └── ui_label.py
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
- **`scenes/menu_scene.py`**: permite iniciar el ejemplo interactivo o salir.
- **`scenes/interaction_scene.py`**: permite modificar el contador y pasar su
  valor a la pantalla de resultado.
- **`scenes/result_scene.py`**: muestra el valor final y permite volver al menú.
- **`components/`**: contiene los componentes reutilizables de botón y etiqueta.

## Flujo

`__main__` llama a `app`, que crea el juego y muestra el menú. Desde allí, el
usuario abre la escena de interacción y guarda el contador para mostrarlo en la
escena de resultado. El ciclo principal entrega los eventos y la superficie de
dibujo a la escena activa; cada escena actualiza su estado y dibuja un fotograma.
Cerrar la ventana o pulsar Escape vuelve al menú o termina el ciclo, según la
escena activa.

Las entidades, sistemas y recursos externos se agregarán cuando haya una
funcionalidad que los necesite. Así la base se mantiene simple y las dependencias
apuntan desde el arranque hacia los módulos de juego, no al revés.
