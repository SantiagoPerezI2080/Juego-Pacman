# models/entities/ghost.py

from typing import Tuple, List
import copy
import random

class Ghost:
    """
    Representa un fantasma enemígo.
    Implementa Prototype Pattern vía método clone().
    """

    def __init__(self, position: Tuple[int, int]):
        self.position: Tuple[int, int] = position

    def move(self, walls: List[List[int]]) -> None:
        """
        IA simple: elige aleatoriamente una de las cuatro direcciones posibles
        que no choque contra un muro.
        """
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = self.position[0] + dx
            new_y = self.position[1] + dy
            if walls[new_y][new_x] == 0:
                self.position = (new_x, new_y)
                break

    def clone(self) -> 'Ghost':
        """
        Prototype Pattern: devuelve una copia profunda del fantasma.
        """
        return copy.deepcopy(self)
