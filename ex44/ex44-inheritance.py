# Inheritance and Composition Example

class Parent(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def whoAmI(self):
        print(f"My name is {self.name}, and I am a parent.")

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def whoAmI(self):
        print(f"My name is {self.name} and I am a child.")
        super().whoAmI()

class Grandchild(Child):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent

    def whoAmI(self):
        print(f"My name is {self.name} and I am a grandchild.")
        print("And this is my parent's info:")
        self.parent.whoAmI()

parent1 = Parent("Greg")
child1 = Child("Liam")
grandchild1 = Grandchild("Stacy", child1)

print("\nParent output")
parent1.whoAmI()
print("\nChild output")
child1.whoAmI()
print("\nGrandchild output")
grandchild1.whoAmI()
