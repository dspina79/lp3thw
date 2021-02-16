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
        self.items.append(Item("Ceiling Fan", 200))
        self.items.append(Item("Sedan", 30000))
        self.items.append(Item("Rice-a-Roni 5 Pack", 10))
        self.items.append(Item("Cuisanart", 49))
        self.items.append(Item("Instapot", 80))
        self.items.append(Item("Encyclopedia Britanica", 1000))
        self.items.append(Item("Tent for 2", 100))
        self.items.append(Item("Stereo", 400))
        self.items.append(Item("Push Lawnmower", 399))

    def get_item(self):
        if len(self.items)> 0:
            item = self.items.pop()
            return item
        else:
            print("No more items.")
            GameEnd("Closing").results()
            return None

class Engine(object):
    def __init__(self, item_rack, main_player, comp_players, game):
        super().__init__()
        self.item_rack = item_rack
        self.main = main_player
        self.other_players = comp_players
        self.game = game
    
    def run(self):
        item = self.item_rack.get_item()
        startingScene = GameScene("The Price is Close")
        startingScene.welcome()
        while item != None:
            instance = GamePlayInstance(item.name)
            instance.play(item, self.main, self.other_players, self.game.host)

class GuessPrice(object):
    def __init__(self, item, player, guess):
        self.player = player
        self.guess = guess
        self.item = item
    
    def difference(self):
        return self.item.get_price() - self.guess

class GameScene(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def welcome(self):
        print(f"Welcome to {self.name}")

class GamePlayInstance(GameScene):
    def __init__(self, name):
        super().__init__(name)

    def play(self, item, main_player, other_players, host):
        print(f"The current item is {item.name}")
        guesses = []

        for other in other_players:
            guess_price = other.guess_price(item)
            guess = GuessPrice(item, other, guess_price)
            print(f"{other.name} guesses ${guess_price}.")
            guesses.append(guess)

        
        player_guess = int(input("What is your guess? "))
        my_guess = GuessPrice(item, main_player, player_guess)
        guesses.append(my_guess)

        the_winner = self.get_winner(guesses)
        # print out simulating the host
        print(f"{host.name}: The actual price is ${item.get_price()}")
        
        if the_winner != None:
            print(f"{host.name}: The winner is: {the_winner.name}")
        else:
            print(f"{host.name}: Sorry, there were no winners. You all suck.")

    def get_winner(self, price_guesses):
        player_win = None
        top_difference = 100000000
        for price_guess in price_guesses:
            if price_guess.difference() > 0 and price_guess.difference() <= top_difference:
                top_difference = price_guess.difference()
                player_win = price_guess.player
                player_win.win()
            else:
                price_guess.player.lose()
         
        return player_win

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
        self.host = Host("Wink Winkelman")
        self.other_players = [Player("Norm"), Player("Sheryl"), Player("Monique")]

    def start(self):
        this_player_name = input("What is your name? ")
        self.main_player = Player(this_player_name)
        self.host.intro(self.other_players, self.main_player)
        self.item_rack = ItemRack()
        self.item_rack.load_items()
        self.engine = Engine(self.item_rack, self.main_player, self.other_players, self)
        self.engine.run()


def main():
    game = Game()
    game.start()

main()


    