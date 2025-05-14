# views/game_view.py

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    TILE_SIZE, FPS, COLOR_BG,
    COLOR_WALL, COLOR_FOOD, COLOR_POWER,
    COLOR_PACMAN, COLOR_GHOST
)

class GameView:
    def __init__(self, model):
        self.model = model

    def init_pygame(self) -> None:
        pygame.init()
        # Configura la ventana con el tamaño del mapa
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        # Inicializar la fuente del HUD
        pygame.font.init()

    def process_events(self, pacman) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                # Dirección: flechas
                if event.key == pygame.K_UP:
                    pacman.set_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    pacman.set_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    pacman.set_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    pacman.set_direction(1, 0)
        return True

    def render(self, model) -> None:
        # Fondo
        self.screen.fill(COLOR_BG)

        # Muros
        for y, row in enumerate(model.walls):
            for x, cell in enumerate(row):
                if cell == 1:
                    rect = pygame.Rect(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    pygame.draw.rect(self.screen, COLOR_WALL, rect)

        # Comida normal
        for x, y in model.food:
            center = (
                x * TILE_SIZE + TILE_SIZE // 2,
                y * TILE_SIZE + TILE_SIZE // 2
            )
            pygame.draw.circle(
                self.screen,
                COLOR_FOOD,
                center,
                TILE_SIZE // 6
            )

        # (Opcional) Comida de poder si la detectas como distinto de '.'
        # Por defecto no hay en el builder; si la añades,
        # model.power_food podría iterarse aquí con COLOR_POWER.

        # Pac‑Man
        px, py = model.pacman.position
        center_p = (
            px * TILE_SIZE + TILE_SIZE // 2,
            py * TILE_SIZE + TILE_SIZE // 2
        )
        pygame.draw.circle(
            self.screen,
            COLOR_PACMAN,
            center_p,
            TILE_SIZE // 2
        )

        # Fantasmas
        for ghost in model.ghosts:
            gx, gy = ghost.position
            center_g = (
                gx * TILE_SIZE + TILE_SIZE // 2,
                gy * TILE_SIZE + TILE_SIZE // 2
            )
            pygame.draw.circle(
                self.screen,
                COLOR_GHOST,
                center_g,
                TILE_SIZE // 2
            )

        # HUD (puntuación)
        model.score_display.draw(self.screen)

        # Actualizar pantalla y controlar FPS
        pygame.display.flip()
        self.clock.tick(FPS)

    def quit(self) -> None:
        pygame.quit()
