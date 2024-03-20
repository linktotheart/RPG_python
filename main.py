from character import Character

hero = Character("Hero", 100, 20)
goblin = Character("Goblin", 50, 12)

while True:
    hero.attack(goblin)
    goblin.attack(hero)

    print(f"{hero.name} has {hero.hp} HP left")
    print(f"{goblin.name} has {goblin.hp} HP left")
    input("Press Any key to continue...")

