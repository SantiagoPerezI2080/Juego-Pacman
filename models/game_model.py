""" # models/game_model.py

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
        self.ghosts = [Ghost(pos) for pos in random.sample(libres, 1)]
    
    def check_collision_with_ghosts(self) -> bool:
        for ghost in self.ghosts:
            if ghost.position == self.pacman.position:
                return True
        return False

    def update(self) -> None:
        # Guarda posiciones anteriores
        pacman_prev = self.pacman.position
        ghosts_prev = [ghost.position for ghost in self.ghosts]

        # 1) Mover Pac‑Man
        self.pacman.move(self.walls)

        # 2) Mover fantasmas
        for ghost in self.ghosts:
            ghost.move(self.walls)

        # 3) Comprobar colisión directa
        if self.check_collision_with_ghosts():
            self.game_over = True
            return

        # 4) Comprobar colisión cruzada (swap)
        for ghost, ghost_prev in zip(self.ghosts, ghosts_prev):
            if self.pacman.position == ghost_prev and pacman_prev == ghost.position:
                self.game_over = True
                return

        # 5) Recolectar comida
        if self.pacman.position in self.food:
            self.food.remove(self.pacman.position)
            self.score_display.score += 10 """

import random
from services.level_loader import LevelBuilder
from ui.score_display import ScoreDisplay
from .entity_manager import EntityManager
from .collision_manager import CollisionManager
from .score_manager import ScoreManager

class GameModel:
    def __init__(self, level_file: str):
        builder = LevelBuilder(level_file)
        walls, food, entities = builder.build()
        self.score_display = ScoreDisplay()
        self.entity_manager = EntityManager(walls, food, entities)
        self.collision_manager = CollisionManager(self.entity_manager)
        self.score_manager = ScoreManager(self.entity_manager, self.score_display)
        self.game_over = False

    def update(self) -> None:
        pacman_prev = self.entity_manager.pacman.position
        ghosts_prev = [ghost.position for ghost in self.entity_manager.ghosts]

        self.entity_manager.update_entities()

        if self.collision_manager.check_pacman_ghost_collision():
            self.game_over = True
            return

        if self.collision_manager.check_swap_collision(pacman_prev, ghosts_prev):
            self.game_over = True
            return

        self.score_manager.collect_food()