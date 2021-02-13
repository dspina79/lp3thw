# The Price is 'Close'
# A game similar to Price is right

from random import randint

class Item(object):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
    
    def get_price(self):
        ten_percent = int(float(self.base_price) * 0.10) 
        if ten_percent > 0:
            return self.base_price + randint(ten_percent * -1, ten_percent)
        return self.base_price

class Person(object):
    def __init__(self, name):
        self.name = name

class Host(Person):
    def __init__(self, name):
        super().__init__(name)

    def intro(self, other_players, main_player):
        print(f"Welcome to the 'Price is Close'. I'm your host, {self.name}")
        print("Today we have four great contestants.")
        for other in other_players:
            print(f"{other.name}")
        print(f"And a fan favorite, {main_player.name}")

        print("Let's get the game started.")

    def present_item(self, item, item_index):
        intro_text = "Next up" 
        if item_index == 1:
            intro_text = "First up"

        print(f"{intro_text}, we have a lovely {item.name}. Let's get bidding.")


class Player(Person):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
        self.knowledge = randint(5, 100)
        self.current_guess = 0

    def win(self):
        self.points += 1
    
    def lose(self):
        self.points += 1

    def guess_price(self, item):
        base_guess = int(float(item.get_price()) * (float(self.knowledge) / 100.00))
        self.current_guess = base_guess + randint(-5, 5)
        return self.current_guess

class ItemRack(object):
    def __init__(self):
        self.items = []
        
    def load_items(self):
        self.items.appen(Item("Ceiling Fan", 200))
        self.items.appen(Item("Sedan", 30000))
        self.items.appen(Item("Rice-a-Roni 5 Pack", 10))
        self.items.appen(Item("Cuisanart", 49))
        self.items.appen(Item("Instapot", 80))
        self.items.appen(Item("Encyclopedia Britanica", 1000))
        self.items.appen(Item("Tent for 2", 100))
        self.items.appen(Item("Stereo", 400))
        self.items.appen(Item("Push Lawnmower", 399))

    def get_item(self):
        if items.count > 0:
            item_index = randint(0, items.count)
            item = self.items[item_index]
            self.items.remove(item)
            return item
        else:
            print("No more items.")
            return None

class Engine(object):
    def __init__(self, item_rack, main_player, comp_players, game):
        super().__init__()
        self.item_rack = item_rack
        self.main = main_player
        self.other_players = comp_players
    
    def run(self):
        item = self.item_rack.get_item()
        while item != None:
            pass

class GameScene(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def welcome(self):
        print(f"Welcome to {name}")

class GamePlayInstance(GameScene):
    def __init__(self, name):
        super().__init__(name)

    def play(self, item, main_player, other_players):
        print(f"The current item is {item.name}")

        for other in other_players:
            print(f"{other.name} guesses ${other.guess_price}.")
        
        player_guess = input(input("What is your guess? "))
        # TODO: Complete

class GameEnd(GameScene):
    def __init__(self, name):
        super().__init__(name)

    def results(self, main_player, other_players):
        self.welcome()
        print("The game is over. Here are the results:")
        top_player = None
        for other in other_players:
            print(f"{other.name}:\t\t{other.points}")
            if top_player == None or other.points > top_player:
                top_player = other
        
        print(f"Your score:\t\t\{main_player.points}")
        if main_player.points >= top_player.points:
            print("YOU WIN!!! Congratulations on a job well done!")
        else:
            print(f"{top_player.name} won. Please try again later.")


class Game(object):
    def __init__(self):
        super().__init__()
        host = Host("Wink Winkelman")
        other_players = [Player("Norm"), Player("Sheryl"), Player("Monique")]

    def start(self):
        this_player_name = input("What is your name? ")
        self.main_player = Player(this_player_name)
        self.host.intro(self.other_players, self.main_player)
        self.item_rack = ItemRack()
        self.item_rack.load_items()
        self.engine = Engine(self.item_rack, self.main_player, self.other_players, self)
    