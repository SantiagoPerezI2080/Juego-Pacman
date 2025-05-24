class ScoreManager:
    def __init__(self, entity_manager, score_display):
        self.entity_manager = entity_manager
        self.score_display = score_display

    def collect_food(self):
        pacman = self.entity_manager.pacman
        food = self.entity_manager.food
        if pacman.position in food:
            food.remove(pacman.position)
            self.score_display.score += 10