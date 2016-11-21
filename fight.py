from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell

class Fight:

	def __init__(self, hero, enemy):
		self.hero = hero
		self.enemy = enemy

	def damage_source(self):
		if not(self.hero.is_equipted()) and not(self.hero.is_learned()):
			return 'Your hero is doomed  - no spell and no weapon.'
		if not(self.hero.is_equipted()):
			if self.hero.get_mana() >= self.hero.spell.get_mana_cost():
				return 'spell'
			return 'Your hero has only spell, but noth enough mana.'
		if not(self.hero.is_learned()):
			return 'weapon'
		if self.hero.spell.get_damage() >= self.hero.weapon.get_damage() and self.hero.get_mana() >= self.hero.spell.get_mana_cost():
				return 'spell'
		return 'weapon'

	def start_fight(self):
		print('Start a fight between Hero: heath= {} mana= {} and Enemy: heath= {} mana= {} damage= {}'
			.format(self.hero.get_health(), self.hero.get_mana(), self.enemy.get_health(), self.enemy.get_mana(), self.enemy.get_damage()))

		while True: #self.enemy.is_alive == True or self.hero.is_alive == True

			if self.damage_source() == 'spell':
				self.enemy.take_damage(self.hero.attack(by='spell'))
				print('Hero casts a {}, hits enemy for {} dmg. Enemy Health is {}'.format(self.hero.spell, self.hero.spell.get_damage(), self.enemy.get_health()))
			elif self.damage_source() == 'weapon':
				self.enemy.take_damage(self.hero.attack(by='weapon'))
				print('Hero hits with {} for {} dmg. Enemy health is {}'.format(self.hero.weapon, self.hero.weapon.get_damage(), self.enemy.get_health()))
			else:
				print(self.damage_source())

			if self.enemy.is_alive() == False:
				print('Enemy is Dead!')
				break

			self.hero.take_damage(self.enemy.get_damage())
			print("Enemy hits hero for {} dmg. Hero health is {}.".format(self.enemy.get_damage(), self.hero.get_health()))

			if self.hero.is_alive() == False:
				print('Game Over your hero is dead!')
				break
