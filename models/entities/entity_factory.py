# models/entities/entity_factory.py

from typing import Optional, Tuple
from models.entities.pacman import Pacman
from models.entities.ghost import Ghost

def create_entity(symbol: str, position: Tuple[int, int]) -> Optional[object]:
    """
    Factory Pattern: crea y retorna la instancia
    adecuada según el símbolo leído del mapa:
      - 'P' → Pacman
      - 'G' → Ghost
      - otro  → None
    """
    if symbol == 'P':
        return Pacman(position)
    elif symbol == 'G':
        return Ghost(position)
    else:
        return None
