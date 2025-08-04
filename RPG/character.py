class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.inventory = []

    def display_stats(self):
        print(f"Name: {self.name}, Health: {self.health}, Strength: {self.strength}")
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory.")
    
    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Used {item}.")
        else:
            print(f"Item {item} not found in inventory.")
