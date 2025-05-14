# models/game_model.py

from typing import List, Tuple
from services.level_loader import LevelBuilder
from ui.score_display import ScoreDisplay

class GameModel:
    def __init__(self, level_file: str):
        builder = LevelBuilder(level_file)
        self.walls, self.food, entities = builder.build()

        # Separar Pac‑Man y fantasmas:
        self.pacman = next(e for e in entities if type(e).__name__ == 'Pacman')
        self.ghosts = [e for e in entities if type(e).__name__ == 'Ghost']

        # HUD
        self.score_display = ScoreDisplay()

    def update(self) -> None:
        # 1) Mover Pac‑Man
        self.pacman.move(self.walls)
        # 2) Recolectar comida
        if self.pacman.position in self.food:
            self.food.remove(self.pacman.position)
            self.score_display.score += 10
        # 3) Mover fantasmas
        for ghost in self.ghosts:
            ghost.move(self.walls)
