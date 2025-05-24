class CollisionManager:
    def __init__(self, entity_manager):
        self.entity_manager = entity_manager

    def check_pacman_ghost_collision(self):
        pacman = self.entity_manager.pacman
        ghosts = self.entity_manager.ghosts
        for ghost in ghosts:
            if ghost.position == pacman.position:
                return True
        return False

    def check_swap_collision(self, pacman_prev, ghosts_prev):
        pacman = self.entity_manager.pacman
        ghosts = self.entity_manager.ghosts
        for ghost, ghost_prev in zip(ghosts, ghosts_prev):
            if pacman.position == ghost_prev and pacman_prev == ghost.position:
                return True
        return False