from dungeon import *
map = Dungeon("level_1.txt")
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip(w)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
h.learn(s)
map.spawn(h)
map.move_hero("right")
map.move_hero("down")