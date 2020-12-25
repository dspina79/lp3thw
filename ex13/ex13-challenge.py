# Exercise 13 Challenge
from sys import argv

script, command = argv

if command == "greet":
    name = input("What is your name? ")
    print(f"Hello {name}!")
else:
    favorite_color = input("What is your favorite color? ")
    print(f"You chose {command}. Your favorite color is {favorite_color}.")

print("End of program")