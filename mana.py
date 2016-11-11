from treasure import Treasure
# from hero import Hero


class Mana(Treasure):
    def __init__(self, mana_points):
        self.mana_points = mana_points

    def apply_on_hero(self, hero):
        hero.take_mana(self.mana_points)
