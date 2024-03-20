from weapon import dagger

class Character:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp
		self.max_hp = hp

		self.weapon = dagger
	
	def attack(self, other_character) -> None:
		other_character.hp -= self.weapon.damage
		other_character.hp = 0 if other_character.hp < 0 else other_character.hp


class Hero(Character):
	def __init__(self, name: str, hp: int):
		super().__init__(name, 100)
		self.weapon = sword