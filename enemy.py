from weapon import Weapon
from spell import Spell

class Enemy:

	def __init__(self,health, mana, damage):
		self.health = health
		self.mana = mana
		self.damage = damage

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

		if current_mana >= mana_cost:
			return True
		return False	

	#the amount of the damage that our character takes 
	def take_damage(self,damage):

		if self.health < damage:
			self.health = 0
		else:
			self.health -= damage

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


	def equip(weapon):
		pass

	def learn(spell):
		pass
		
	def  attack(self, attacks):

		#if attacks == 'weapon':
		#	return self.damage + weapon_damage
		#elif attacks == 'magic':
		#	return self.damage + spell_dmg
			



