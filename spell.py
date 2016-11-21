from treasure import Treasure
# from hero import Hero


class Spell(Treasure):

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.damage, self.mana_cost, self.cast_range)

    def __repr__(self):
        return self.__str__()

    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range

    def apply_on_hero(self, hero):
        hero.learn(self)

    @classmethod
    def create_spell(cls, descr):  # descr is the needed attributes as string
        spell_attr = descr.split(' ')
        cast_range = int(spell_attr[-1])
        mana_cost = int(spell_attr[-2])
        damage = int(spell_attr[-3])
        del spell_attr[-3:]  # removes last three elements
        name = " ".join(spell_attr)  # everything else is the spell name
        return Spell(name, damage, mana_cost, cast_range)
