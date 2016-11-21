from weapon import Weapon
from spell import Spell

class Enemy:

	def __init__(self,health, mana, damage):
		self.health = health
		self.mana = mana
		self.damage = damage
		self.current_health = health
		self.current_mana = mana
		self.spell = None
		self.weapon = None

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

		if self.spell is not None and self.current_mana >= self.spell.mana_cost():
			return True
		return False

	#the amount of the damage that our character takes
	def take_damage(self,damage):

		if self.current_health < damage:
			self.current_health = 0
		else:
			self.current_health -= damage

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


	def equip(self, weapon):

		self.weapon = weapon

	def learn(self, spell):

		self.spell = spell

	def attack(self, by='None'):

		if by == 'weapon':
			return self.damage + self.weapon.get_damage()
		if by == 'spell':
			if self.mana < self.spell.get_mana_cost():
				return False
			else:
				self.mane -= self.spell.get_mana_cost()
				return self.damage + self.spell.get_damage()
