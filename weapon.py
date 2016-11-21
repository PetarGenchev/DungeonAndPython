from treasure import Treasure
# from hero import Hero

class Weapon(Treasure):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def get_damage(self):
        return self.damage

    def apply_on_hero(self, hero):
        hero.equip(self)

    @classmethod
    def create_weapon(cls, descr):  # descr is the needed atributes as string
        weapon_attr = descr.split(' ')
        damage = int(weapon_attr[-1])  # last word in descr has to be a number
        weapon_attr.pop()
        name = " ".join(weapon_attr)  # everything exept the last word is the name
        return Weapon(name, damage)
