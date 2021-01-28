# Animals

# Animal base object

class Animal(object):
    pass

# Dog - an subclass of an Animal (is-a)
class Dog(Animal):
    # construator (has-a)
    def __init__(self, name):
        super().__init__()
        # instantiate with the name defined
        self.name = name

    def bark(self):
        print(f"{self.name} is barking.")

# Cat - an subclass of an Animal (is-a)
class Cat(Animal):
    # construator (has-a)
    def __init__(self, name):
        super().__init__()
        # instantiate with the name defined
        self.name = name

# Person - a base class
class Person(object):
    # constructor (has-a)
    def __init__(self, name):
        self.name = name
        # Person has-a Pets
        self.pet = []
        self.kids = {}

    def introduce(self):
        print(f"Hello. My name is, {self.name}.")

    def display_kids(self):
        print(f"These are the children of {self.name}")
        for kid, age in list(self.kids.items()):
            print(f"\t{kid} is {age} years old.")

# Employee - a subclass of Person (is-a)
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish - a base class
class Fish(object):
    pass

# Salmon - a subclass of Fish (is-a)
class Salmon(Fish):
    pass

# Halibut - a subclass of Fish (is-a)
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# Peppy is-a Cat
peppy = Cat("Peppy")

# Mary is-a Person
mary = Person("Mary")

# Mary has-a pet, specifically Peppy
mary.pet.append(peppy)

mary.introduce()
mary.kids["Timmy"] = 5
mary.kids["Johnny"] = 12
mary.kids["Lisa"] = 14

# show Mary's kids
mary.display_kids()

# Frank is-a Employee
frank = Employee("Frank", 120000)

# Frank has a pet, specifically, Rover
frank.pet.append(rover)
frank.introduce()
frank.pet[0].bark()

# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut
harry = Halibut()
