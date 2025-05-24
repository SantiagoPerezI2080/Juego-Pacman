# main.py
import pygame
import os
from controllers.game_controller import GameController
from config import MAP_FILE



if __name__ == '__main__':
    # Construye la ruta absoluta al mapa
    level_path = os.path.join(os.path.dirname(__file__), MAP_FILE)
    controller = GameController(level_path)
    controller.run()
