import sys
from hero import Hero
from collector import Collector
from point import get_neighbor, point_is_passable

levels = ["level_1.txt", "level_2.txt"]
levels_count = 2


class Dungeon:
    def __init__(self, file_name):
        self.map = []
        self.hero = None  # waiting for the first call of spawn(hero)
        self.hero_x = -1
        self.hero_y = -1
        self.collector = Collector()  # collect spawn cells, enemies and treasures
        self.level = levels.index(file_name) + 1
        self._read_file(file_name)

    def print_map(self):
        for line in self.map:
            print("".join(line))

    def spawn(self, hero):
        if self.collector.no_spawn_cells():
            return False
        self.hero = hero
        x, y = self.collector.get_first_spawn_cell()
        self._move_hero_in_map(x, y)
        return True

    def move_hero(self, direction):
        x, y = get_neighbor(self.hero_x, self.hero_y, direction)
        if point_is_passable(self.map, x, y):
            self._do_step(x, y)
            return True
        else:
            return False

    def _do_step(self, x, y):
        self._move_into(x, y)  # cheks if map[x][y] is T, E or G
        self.hero.regan_mana_after_move()
        self._move_hero_in_map(x, y)

    def _move_into(self, x, y):
        symbol = self.map[x][y]
        if symbol == 'T':
            self.treasures[(x, y)].apply_on_hero(self.hero)
        # elif symbol == 'E':
        #     Fight(self.hero, self.enemies[(x, y)])
        if self._is_game_over():
            print("Game over!")
            sys.exit(0)
        # elif symbol == 'G':
        #   self._go_on_next_level()

    def _move_hero_in_map(self, x, y):
        if self.hero_x >= 0 and self.hero_y >= 0:
            self.map[self.hero_x][self.hero_y] = '.'
        self.hero_x = x
        self.hero_y = y
        self.map[x][y] = 'H'

    def _is_game_over(self):
        hero_is_dead = not(self.hero.is_alive())
        no_spawn_cells = self.collector.no_spawn_cells()
        return no_spawn_cells and hero_is_dead

    def _go_on_next_level(self):
        if self.level == levels_count:
            print("Congrats!!!")
            sys.exit(0)
        else:
            self._read_file(levels[self.level])
            self.spawn(self.hero)
            self.levels += 1

    def _read_file(self, file_name):
        self.map = []
        self.collector.clear_data()
        with open(file_name, 'r') as f:
            content = f.readlines()
            for i in range(len(content)):
                line = []
                line_input = content[i].rstrip('\n')
                for j in range(len(line_input)):
                    self._read_symbol(line, line_input[j], i, j)
                self.map.append(line)

    def _read_symbol(self, symbols_list, symbol, i, j):
            if symbol == 'S':
                self.collector.add_spawn_cell(i, j)
            if symbol == 'E':
                self.collector.add_enemy_at_pos(i, j)
            if symbol == 'T':
                self.collector.add_treasure_at_pos(i, j)
            symbols_list.append(symbol)
