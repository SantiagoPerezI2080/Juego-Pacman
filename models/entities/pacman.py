# models/entities/pacman.py

from typing import Tuple, List

class Pacman:
    """
    Representa al jugador Pac‑Man.
    """

    def __init__(self, position: Tuple[int, int]):
        self.position: Tuple[int, int] = position
        # Dirección actual (dx, dy). Empieza sin moverse.
        self.direction: Tuple[int,int] = (0, 0)

    def set_direction(self, dx: int, dy: int) -> None:
        """
        Actualiza la dirección deseada (p. ej. llamada desde GameView).
        """
        self.direction = (dx, dy)

    def move(self, walls: List[List[int]]) -> None:
        """
        Intenta mover a Pac‑Man en la dirección actual,
        si la celda destino no es muro.
        """
        dx, dy = self.direction
        if dx == dy == 0:
            return  # sin movimiento

        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        # Comprueba que no choque contra un muro
        if walls[new_y][new_x] == 0:
            self.position = (new_x, new_y)
