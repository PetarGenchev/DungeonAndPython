from treasure import Treasure
# from hero import Hero


class Health(Treasure):
    def __init__(self, health_points):
        self.health_points = health_points

    def apply_on_hero(self, hero):
        hero.take_healing(self.health_points)
