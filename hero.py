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
		return '{} the {}'.format(self.name, self.title)

	#return the current health points of the character
	def get_health(self):
		return self.health

	#return the current mana points of character
	def get_mana(self):
		return self.mana

	#return if the character is alive
	def is_alive(self):

		if self.health <= 0:
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
	
	#for every step incrase the current mana with the mana regen given
	def regen_mana_after_move(self):
		new_point = get_neighbor(direction)
		if is_point_passable == get_neighbor(direction):
			current_mana += mana_regeneration_rate
		
		
	def equip(self, weapon):
		self.weapon = weapon
		
		
	def learn(self, spell):
		
		self.spell = spell
	
	def attack(self, by='None'):
		
		if by == 'weapon':
			return self.damage + self.weapon.get_damage()
		if by == 'spell':
			if self.mana >= self.spell.get_mana_cost():
				self.mane -= self.spell.get_mana_cost()
				return self.damage + self.spell.get_damage()
			return False

	def is_equipted(self):
		return self.weapon is not None


	def is_learned(self):
		return self.spell is not None