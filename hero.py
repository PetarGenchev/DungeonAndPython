from weapon import Weapon
from spell import Spell

class Hero:

	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		self.name = name
		self.title = title
		self.health = health
		self.mana = mana
		self.mana_regeneration_rate = mana_regeneration_rate
		self.current_health = health
		self.current_mana = mana
		self.spell = None
		self.weapon = None

	#return the name and title of the character
	def known_as(self):
		return '{} the {}'.format(self.name, self.title)

	#return the current health points of the character
	def get_health(self):
		return self.current_health

	#return the current mana points of character
	def get_mana(self):
		return self.current_mana

	#return if the character is alive
	def is_alive(self):

		if self.current_health <= 0:
			return False
		return True

	#check if the character got enough mana points to cast spell
	def can_cast(self):
		if self.current_mana == 0:
			return 'Can\'t cast the current mana is 0'
		elif self.spell is not None and self.current_mana >= self.spell.get_mana_cost():
			return True
		return False

	#the amount of the damage that our character takes
	def take_damage(self,damage_point):

		if self.current_health < damage_point:
			self.current_health = 0
		else:
			self.current_health -= damage_point

	#check if our character can be healed
	def take_healing(self,healing_point):

		if self.current_health <= 0:
			return False
		self.current_health += healing_point
		if self.current_health > self.health:
			self.current_health = self.health
		return True

	#check if our character can regen mana
	def take_mana(self, mana_point):

		self.current_mana += mana_point
		if self.current_mana > self.mana:
			self.current_mana = self.mana

	#for every step incrase the current mana with the mana regen given
	def regan_mana_after_move(self):
		self.current_mana += self.mana_regeneration_rate


	def equip(self, weapon):
		self.weapon = weapon


	def learn(self, spell):

		self.spell = spell

	def attack(self, by='None'):

		if by == 'weapon':
			return self.weapon.get_damage()
		if by == 'spell':
			if self.current_mana >= self.spell.get_mana_cost():
				self.current_mana -= self.spell.get_mana_cost()
				return self.spell.get_damage()
			return False

	def is_equipted(self):
		return self.weapon is not None


	def is_learned(self):
		return self.spell is not None
