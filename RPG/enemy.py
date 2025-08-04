import random

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.max_health = health
        self.memory = {"attack": 0, "defend": 0, "flee": 0}

    def learn_player_move(self, action):
        if action in self.memory:
            self.memory[action] += 1

    def analyze_behavior(self):
        if self.memory["attack"] > self.memory["defend"]:
            print(f"{self.name} has learned! It starts dodging more.")
            return "dodge"
        elif self.memory["defend"] > self.memory["attack"]:
            print(f"{self.name} has learned! It uses more grabs to counter defense.")
            return "grab"
        return "normal"

    def check_health(self):
        return self.health < 0.3 * self.max_health

    def heal(self):
        heal_amount = random.randint(5, 15)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} HP! Now at {self.health} HP.")

    def attack(self, player_choice):
        self.learn_player_move(player_choice)

        if self.check_health():
            self.heal()
            return

        strategy = self.analyze_behavior()
        if strategy == "dodge":
            print(f"{self.name} dodges your attack!")
            return

        elif strategy == "grab":
            print(f"{self.name} counters your defense with a powerful grab!")
            return

        if random.random() < 0.3:
            return self.special_attack()
        else:
            damage = random.randint(1, self.strength)
            print(f"{self.name} attacks normally for {damage} damage.")
            return damage

    def special_attack(self):
        damage = random.randint(self.strength, self.strength * 2)
        print(f"{self.name} uses a special attack dealing {damage} damage!")
        return damage


class Goblin(Enemy):  
    def __init__(self):
        super().__init__("Goblin", health=30, strength=5)

    def special_attack(self):
        damage = random.randint(self.strength, self.strength * 2)
        print(f"{self.name} uses a special attack dealing {damage} damage!")
        return damage

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", health=50, strength=10)

    def special_attack(self):
        damage = random.randint(self.strength * 2, self.strength * 3)
        print(f"{self.name} smashes you with a heavy club, dealing {damage} damage!")
        return damage   

class Dragon(Enemy):  
    def __init__(self):
        super().__init__("Dragon", health=100, strength=15)  
    
    def special_attack(self):
        damage = random.randint(self.strength * 3, self.strength * 5)
        print(f"{self.name} breathes fire, dealing {damage} damage!")
        return damage

goblin = Goblin()
orc = Orc()
dragon = Dragon()

goblin.special_attack()  
orc.special_attack()  
dragon.special_attack()
    

