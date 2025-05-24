# models/game_model.py

import random
from typing import List, Tuple
from services.level_loader import LevelBuilder
from ui.score_display import ScoreDisplay
from models.entities.ghost import Ghost # Importa la clase Ghost


class GameModel:
    def __init__(self, level_file: str):
        builder = LevelBuilder(level_file)
        self.walls, self.food, entities = builder.build()

        # Separar Pac‑Man y fantasmas:
        self.pacman = next(e for e in entities if type(e).__name__ == 'Pacman')
        self.ghosts = [e for e in entities if type(e).__name__ == 'Ghost']

        # HUD
        self.score_display = ScoreDisplay()

        #Agregando un atributo para el estado del juego
        self.game_over = False

        # --- POSICIONES ALEATORIAS PARA 4 FANTASMAS ---
        # Encuentra todas las posiciones libres (sin muro ni Pac-Man)
        libres = [
            (x, y)
            for y, row in enumerate(self.walls)
            for x, cell in enumerate(row)
            if cell == 0 and (x, y) != self.pacman.position
        ]
        # Elige 4 posiciones aleatorias distintas
        self.ghosts = [Ghost(pos) for pos in random.sample(libres, 3)]



    def update(self) -> None:
        # 1) Mover Pac‑Man
        self.pacman.move(self.walls)

        # 2) Comprobar colisión con fantasmas
        if self.check_collision_with_ghosts():
            self.game_over = True

        # 3) Recolectar comida
        if self.pacman.position in self.food:
            self.food.remove(self.pacman.position)
            self.score_display.score += 10

        # 4) Mover fantasmas
        for ghost in self.ghosts:
            ghost.move(self.walls)


       #5) Comprobar colisión con fantasmas
    def check_collision_with_ghosts(self) -> bool:
        for ghost in self.ghosts:
            if ghost.position == self.pacman.position:
                return True
        return False