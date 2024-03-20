class Weapon:
	def __init__(self, name: str, type: str, damage: int, value: int):
		self.name = name
		self.type = type
		self.damage = damage
		self.value = value


claymore = Weapon("Claymore", "Sword", 20, 100)

short_bow = Weapon("Short Bow", "Bow", 10, 50)

dagger = Weapon("Dagger", "Knife", 5, 25)