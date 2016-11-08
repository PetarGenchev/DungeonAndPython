from random import randint

class Dungeon:
    treasure_file_name = "treasures.txt"

    def __init__(self, file_name):
        self.map = []
        self.hero = None  # waiting for the first call of spawn(hero)
        self.hero_x = -1
        self.hero_y = -1
        self.spawn_cells = []
        read_file(file_name)

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            content = f.readlines()
            for i in range(len(content)):
                j = 0
                line = []
                for symbol in line_input.rstrip('\n'):
                    if symbol == 'S':
                        self.spawn_cells.append([i, j])
                    j += 1
                    line.append(symbol)
                self.map.append(line)

    def print_map(self):
        for line in self.map:
            print("".join(line))

    def spawn(hero):
        if self.spawn_cells == []:
            return False
        self.hero = hero
        x = self.spawn_cells[0][0]
        y = self.spawn_cells[0][1]
        move_hero_in_map(x, y)
        self.spawn_cells.pop(0)
        return False

    def is_point_passable(self, x, y):
        rows = len(self.map)
        cols = len(self.map[0])
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        return self.map[x][y] != '#'

    def go_to_point(self, x, y):
        symbol = self.map[x][y]
        if symbol == 'T':
            pick_treasure()
        # elif symbol == 'E':
        #
        # elif symbol == 'G':
        #
        move_hero_in_map(x, y)

    def pick_treasure(self):
        with open(treasure_file_name, 'r') as f:
            content = f.readlines()
            count = len(content)
            index = randint(0, count - 1)
            get_treasure(content[index])

    def get_treasure(self, treasure):  # not tested yet :D
        kind = treasure.split(':')[0].rstrip(' ')
        description = treasure.split(':')[1]
        if kind == "weapon":
            w_list = description.split(' ')
            damage = int(w_list[-1])
            w_list.pop()
            w = Weapon(" ".join(w_list), damage)
            self.hero.equip(w)
        elif kind == "spell":
            s_list = description.split(' ')
            cast_range = int(s_list[-1])
            mana_cost = int(s_list[-2])
            damage = int(s_list[-3])
            s_list.pop()
            s_list.pop()
            s_list.pop()
            s = Spell(" ".join(s_list), damage, mana_cost, cast_range)
            self.hero.learn(s)
        elif kind == "mana":
            mana = int(description)
            hero.take_mana(mana)
        elif kind == "health":
            health = int(description)
            hero.take_healing(health)

    def move_hero_in_map(self, x, y):
        self.hero_x = x
        self.hero_y = y
        self.map[x][y] = 'H'

    def move_hero(self, direction):
        new_point = get_neighbor(direction)
        if is_point_passable(new_point[0], new_point[1]):
            go_to_point(new_point[0], new_point[1])
            return True
        else:
            return False

    def get_neighbor(self, direction):
        neighbors = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
        if direction not in neighbors.keys():
            raise ValueError("Direction must be up, down, left or right.")
        new_x = self.hero_x + neighbors[direction][0]
        new_y = self.hero_y + neighbors[direction][1]
        return [new_x, new_y]
