from treasure import Treasure
from enemy import Enemy

class Collector:
    def __init__(self):
        self.clear_data()

    def clear_data(self):
        self.spawn_cells = []  # list of lists with two coordinatess of a spawn cell
        self.enemies = {}  # dict with key - tuple of two indexes and value - Enemy
        self.treasures = {}  # dict with key - tuple of two indexes and value - Treasure

    def no_spawn_cells(self):
        return self.spawn_cells == []

    def get_first_spawn_cell(self):
        x = self.spawn_cells[0][0]
        y = self.spawn_cells[0][1]
        self.spawn_cells.pop(0)
        return x, y

    def add_spawn_cell(self, x, y):
        self.spawn_cells.append([x, y])

    def add_enemy_at_pos(self, x, y):
        self.enemies[(x, y)] = Enemy.create_random_enemy()

    def get_enemy_from_pos(self, x, y):
        return self.enemies[(x, y)]

    def add_treasure_at_pos(self, x, y):
        self.treasures[(x, y)] = Treasure.create_treasure()

    def get_treasure_from_pos(self, x, y):
        return self.treasures[(x, y)]
