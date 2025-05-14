# ui/score_display.py

import pygame
from typing import Any

class ScoreDisplay:
    """
    Muestra el puntaje en pantalla usando Pygame.
    """

    def __init__(self):
        self.score: int = 0

    def draw(self, screen: Any) -> None:
        """
        Dibuja el HUD (puntos) en la esquina superior izquierda.
        """
        # Inicializa la fuente (puede ser lento; en prod convendría crearla una sola vez)
        font = pygame.font.SysFont(None, 24)
        text_surf = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_surf, (10, 10))
