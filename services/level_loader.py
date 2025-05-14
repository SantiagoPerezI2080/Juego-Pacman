# services/level_loader.py

from typing import List, Tuple
from models.entities.entity_factory import create_entity


class LevelBuilder:
    """
    Builder Pattern: carga un nivel desde un archivo de texto
    y construye tres estructuras:
      - walls: matriz de 0/1 indicando muros
      - food: lista de tuplas (x, y) con posiciones de comida
      - entities: lista de objetos Pacman o Ghost
    """

    def __init__(self, level_file: str):
        self.level_file = level_file

    def build(self) -> Tuple[List[List[int]], List[Tuple[int, int]], List]:
        walls: List[List[int]] = []
        food: List[Tuple[int, int]] = []
        entities: List = []

        with open(self.level_file, 'r') as f:
            for y, line in enumerate(f):
                row: List[int] = []
                for x, ch in enumerate(line.rstrip('\n')):
                    if ch == '#':
                        row.append(1)
                    else:
                        row.append(0)
                        if ch == '.':
                            food.append((x, y))
                        elif ch in ('P', 'G'):
                            entity = create_entity(ch, (x, y))
                            if entity is not None:
                                entities.append(entity)
                walls.append(row)

        return walls, food, entities
