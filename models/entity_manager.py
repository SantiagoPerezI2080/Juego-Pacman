import random
from models.entities.ghost import Ghost

class EntityManager:
    def __init__(self, walls, food, entities):
        self.walls = walls
        self.food = food
        self.pacman = next(e for e in entities if type(e).__name__ == 'Pacman')
        self.ghosts = [e for e in entities if type(e).__name__ == 'Ghost']

        # Si quieres fantasmas en posiciones aleatorias:
        libres = [
            (x, y)
            for y, row in enumerate(self.walls)
            for x, cell in enumerate(row)
            if cell == 0 and (x, y) != self.pacman.position
        ]
        # Cambia el número para más fantasmas
        self.ghosts = [Ghost(pos) for pos in random.sample(libres, 4)]

    def update_entities(self):
        self.pacman.move(self.walls)
        for ghost in self.ghosts:
            ghost.move(self.walls)