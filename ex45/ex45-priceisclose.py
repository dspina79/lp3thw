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

class Player(Person):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0

    def win(self):
        self.points += 1
    
    def lose(self):
        self.points += 1

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
    pass

class Game(object):
    pass
        