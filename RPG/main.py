from game_world import GameWorld
from character import Character
from enemy import Enemy
import random


def show_introduction():
    print("Welcome to the world of My RPG!")
    print("In this game, you will explore dangerous lands, fight monsters, and uncover treasures.")
    print("Your journey begins now...")
    print("-" * 40)


def search_room(player, game_world):
    if game_world.current_location in game_world.treasures:
        print(f"You searched the area and found a {game_world.treasures[game_world.current_location]}!")
        player.add_item(game_world.treasures[game_world.current_location])
        del game_world.treasures[game_world.current_location]
    else:
        print("You searched the area but nothing special was found.")

def combat_system(character, enemy):
    print(f"A wild {enemy.name} appears!")

    while character.health > 0 and enemy.health > 0:
        action = input("Do you want to 'attack' or 'flee'? ").lower()
       
        if action == 'attack':
            damage = random.randint(1, character.strength)
            enemy.health -= damage
            print(f"You attack {enemy.name} for {damage} damage.")
           
            if enemy.health > 0:
                damage = random.randint(1, enemy.strength)
                character.health -= damage
                print(f"{enemy.name} attacks you for {damage} damage.")
            else:
                print(f"You defeated {enemy.name}!")
                break

        elif action == 'defend':
            print("You brace yourself for an attack!")
            enemy.attack("defend")
        
        elif action == 'flee':
            print("You fled from the battle.")
            enemy.attack("flee  ")
            break
        else: 
            print("Unknown action. Choose 'attack' or 'flee'.")

def game():
    show_introduction()


    game_world = GameWorld()
    
    
    name = input("Enter your character's name: ")
    player = Character(name)
    print(f"Character created: {player.name}")
    player.display_stats()
    
    
    print(game_world.rooms[game_world.current_location]['description'])
    
    while True:
        command = input("Enter command (or 'quit' to exit): ").lower()
        
        if command == 'quit':
            print("Goodbye! Thanks for playing.")
            break
        
        elif command.startswith('go '):
            direction = command.split()[1]
            game_world.move_player(direction)
        
        elif command == 'stats':
            player.display_stats()
        
        elif command.startswith('use '):
            item = " ".join(command.split()[1:])
            player.use_item(item)

        elif command == 'search':
            search_room(player, game_world)
        
        elif command == 'fight':
            enemy = Enemy(name='Goblin', health=50, strength=5)
            combat_system(player, enemy)
        
        elif command.startswith(
            'take '):
            item = " ".join(command.split()[1:])
            player.add_item(item)
   
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    game()
    input("Press Enter to exit...")


