class Game:
    def __init__(self):
        self.inventory = []
        self.location = "start"
        self.map = {
            "start": {"description": "You are at the start of a maze of twisty passages, all alike.", "north": "kitchen"},
            "kitchen": {"description": "You are in a kitchen. There is a key on the table.", "south": "start", "west": "library"},
            "library": {"description": "You are in a cozy library. There is a guard here.", "east": "kitchen"}
        }

    def start(self):
        print("Welcome to the adventure game!")
        while True:
            print(self.map[self.location]["description"])
            command = input("> ").strip().lower()
            self.parse_command(command)

    def parse_command(self, command):
        #TODO
        '''

        '''
        match command.split():
            case ["go", direction]:
                self.move(direction)
            case ["pick", "up", item]:
                self.pick_up(item)
            case ["talk", "to", character]:
                self.talk_to(character)
            case ["quit"]:
                print("Thanks for playing!")
                exit()
            case _:
                print("I don't understand that command.")

    def move(self, direction):
        if direction in self.map[self.location]:
            self.location = self.map[self.location][direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def pick_up(self, item):
        if "key" in item and self.location == "kitchen":
            self.inventory.append("key")
            print("You picked up the key!")
        else:
            print("There is nothing here to pick up.")

    def talk_to(self, character):
        if "guard" in character and self.location == "library":
            if "key" in self.inventory:
                print("The guard smiles and opens a door for you.")
            else:
                print("The guard grunts and points to the kitchen saying, 'Find the key.'")
        else:
            print("There is no one here to talk to.")

# To play the game, create an instance of Game and call start method
game = Game()
game.start()
