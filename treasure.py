from random import randint

treasures_file_name = "treasures.txt"


class Treasure:
    def apply_on_hero(self, hero):
        pass

    @classmethod
    def create_treasure(cls):
        with open(treasures_file_name, 'r') as f:
            content = f.readlines()
            count = len(content)
            index = randint(0, count - 1)
            return Treasure.get_treasure(content[index])

    @classmethod
    def get_treasure(cls, treasure):  # treasure is the treasure as string
        kind = treasure.split(':')[0].rstrip(' ')  # ':' splits the kind of treasure and it's description
        descr = treasure.split(':')[1]
        if kind == "weapon":
            from weapon import Weapon
            return Weapon.create_weapon(descr)
        if kind == "spell":
            from spell import Spell
            return Spell.create_spell(descr)
        elif kind == "mana":
            from mana import Mana
            return Mana(int(descr))
        elif kind == "health":
            from health import Health
            return Health(int(descr))
        else:
            raise ValueError("Not correct kind of treasure.")
