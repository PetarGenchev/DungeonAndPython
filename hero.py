from weapon import Weapon
from spell import Spell

class Hero:

	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		self.name = name
		self.title = title
		self.health = health
		self.mana = mana
		self.mana_regeneration_rate = mana_regeneration_rate

	#return the name and title of the character
	def known_as(self):
		return self.name + " the " + self.title

	#return the current health points of the character
	def get_health(self,current_health):

		current_health += self.health - damage_point
		return current_health

	#return the current mana points of character
	def get_mana(self,current_mana):

		current_mana += self.mana - mana_cost
		return	current_mana

	#return if the character is alive
	def is_alive(self):

		if current_health <= 0:
			return False
		return True

	#check if the character got enough mana points to cast spell
	def can_cast(self):
		if self.mana == 0:
			return 'Can\'t cast the current mana is 0'
		elif current_mana >= mana_cost:
			return True
		return False

	#the amount of the damage that our character takes
	def take_damage(self,damage_point):

		if self.health < damage_point:
			self.health = 0
		else:
			self.health -= damage_point

	#check if our character can be healed
	def take_healing(self,healing_point):

		if current_health <= 0 and (current_health + healing_point) > self.health:
			return False
		return True,current_health + healing_point

	#check if our character can regen mana
	def take_mana(self, mana_point):

		while self.mana > 0:
			if (current_mana + mana_point) < self.mana:
				return True
			return False


	def regen_mana_after_move(self):
		pass



	def equip(weapon):
		pass

	def learn(spell):
		pass
		#spell = current_spell
		#if current_spell != spell:
		#	current_spell = spell
		#return current_spell

	def attack(by):
		pass
		#if by == 'weapon':
		#	return weapon_damage
		#if by = 'spell':
		#	return spell_damage
