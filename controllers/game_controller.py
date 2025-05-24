# controllers/game_controller.py

import pygame
from models.game_model import GameModel
from views.game_view import GameView

class GameController:
    def __init__(self, level_file: str):
        pygame.init()
        # Configura la ventana con el tamaño del mapa
        self.screen = pygame.display.set_mode((800, 600))
        # Inicializa el controlador del juego
        self.model = GameModel(level_file)
        self.view = GameView(self.model)

    """ def run(self) -> None:
        self.view.init_pygame()
        running = True
        while running:
            # 1) Eventos: set_direction en Pac‑Man
            running = self.view.process_events(self.model.pacman)
            # 2) Lógica de juego
            self.model.update()
            # 3) Renderizado
            self.view.render(self.model)
        self.view.quit()
 """
    def run(self):
        running = True
        while running:
            running = self.view.process_events(self.model.pacman)
            if not self.model.game_over:
                self.model.update()
                self.view.render(self.model)
            else:
                self.view.show_game_over(self.view.screen)
                running = False
