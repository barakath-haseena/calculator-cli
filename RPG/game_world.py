import random


class GameWorld:
    def __init__(self):
        self.rooms = {
            'town_square': {
                'description': 'You are in the town square. People are bustling around.',
                'north': 'forest',
                'south': 'inn',
                'east' : 'cave',
                'west' : 'lake'
            },
            'forest': {
                'description': 'You are in a dark, dense forest. It feels eerie.',
                'south': 'town_square',
                'north' : 'mountain'
            },
            'inn': {
                'description': 'You are in the local inn. The smell of food fills the air.',
                'north': 'town_square'
            },
            'cave': {
            'description' : 'A dark, damp cave with eerie echoes. You sense something lurking within.',
            'west' : 'town_square',
            'north' : 'dungeon'
            },
            'mountain' : {
            'description' : 'The towering mountain pierces the sky. The air is thin, and the path is treacherous.',
            'south' : 'forest',
            'west': 'dungeon'
            },
            'dungeon': {
            'description': 'A ruined dungeon filled with remains of old warriors. You can hear some ditant growls...',
            'south': 'cave',
            'east' : 'mountain'
            },
            'lake' : {
            'description' : 'A peaceful lake with crystal-clear water. The reflection shimmers under the sun.',
            'east' : 'town_square',
            'north' : 'forest'
            }
        }

        self.treasures = self.place_treasures()
        self.current_location = 'town_square'
    
    def place_treasures(self):
        possible_treasures = ['gold coin', 'mysterious gem', 'ancient scroll', 'healing potion']
        return {room: random.choice(possible_treasures) for room in random.sample(list(self.rooms.keys()), k=3)}

    def move_player(self, direction):
        if direction in self.rooms[self.current_location]:
            self.current_location = self.rooms[self.current_location][direction]
            print(f"You moved {direction}.")
            print(self.rooms[self.current_location]['description'])
            if self.current_location in self.treasures:
                print(f"You found a {self.treasures[self.current_location]}!")
                del self.treasures[self.current_location]
        else:
            print(f"You can't go {direction} from here.")
