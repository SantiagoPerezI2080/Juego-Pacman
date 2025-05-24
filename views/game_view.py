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
        # Inicializa la vista del juego
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()

        # Inicializa el modelo del juego
        self.model = model

    def init_pygame(self) -> None:
        pygame.init()
        # Configura la ventana con el tamaño del mapa
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        # Inicializar la fuente del HUD
        pygame.font.init()

        # Vista del juego Game Over
    def show_game_over(self, screen):
        # Crear una capa semitransparente sobre el juego (opcional)
        overlay = pygame.Surface(screen.get_size())
        overlay.set_alpha(180)  # Transparencia (0-255)
        overlay.fill((0, 0, 0))  # Fondo negro
        screen.blit(overlay, (0, 0))

        # Renderizar el texto centrado
        font_size = 48  # Ajusta el tamaño para que no sea tan grande
        font = pygame.font.SysFont(None, font_size)
        text = font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, rect)

        pygame.display.flip()
        pygame.time.wait(3000)  # Esperar 3 segundos antes de cerrar
            


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
        for y, row in enumerate(model.entity_manager.walls):
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
        for x, y in model.entity_manager.food:
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

        # Pac‑Man
        px, py = model.entity_manager.pacman.position
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
        for ghost in model.entity_manager.ghosts:
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


    