class Spell:
    def_name = "Fireball"
    def_damage = 30
    def_mana_cost = 50
    def_cast_range = 2

    def __init__(name=def_name, damage=def_damage,
    mana_cost=def_mana_cost, cast_range=def_cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range
    
