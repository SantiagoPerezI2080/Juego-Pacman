# config.py

"""
Configuración general del juego Pac‑Man.
Ajusta SCREEN_WIDTH y SCREEN_HEIGHT según el tamaño del mapa y TILE_SIZE.
"""

# Número de columnas y filas del mapa
MAP_COLS = 24
MAP_ROWS = 24

# Tamaño de cada celda (en píxeles)
TILE_SIZE = 20

# Tamaño de la ventana (en píxeles)
SCREEN_WIDTH  = MAP_COLS * TILE_SIZE   # 24 columnas × 20 px = 480 px
SCREEN_HEIGHT = MAP_ROWS * TILE_SIZE   # 24 filas   × 20 px = 480 px

# Fotogramas por segundo
FPS = 8

# Ruta relativa al archivo de mapa
MAP_FILE = 'assets/map.txt'

# Colores (RGB)
COLOR_BG       = (0, 0, 0)       # Fondo
COLOR_WALL     = (0, 0, 255)     # Muros
COLOR_FOOD     = (255, 255, 0)   # Comida normal
COLOR_POWER    = (255, 165, 0)   # Comida de poder (naranja)
COLOR_PACMAN   = (255, 255, 0)   # Pac‑Man
COLOR_GHOST    = (255, 0, 0)     # Fantasmas
COLOR_TEXT     = (255, 255, 255) # Texto del HUD

# Velocidades (celdas por movimiento)
PACMAN_SPEED = 0.001
GHOST_SPEED  = 0.001

# Fuente del HUD
HUD_FONT_SIZE = 24
