# Another challenge
from sys import argv

script, command, direction, subcode, argument = argv

if command == "greet":
    name = input("Hello. What is your name? ")
    print(f"You had picked {command} and you are to be greeted. Hello {name}")
elif direction == "up":
    how_far = input(f"You selected {direction}. How far do you want to go? ")
    print(f"You will go {direction} {how_far} units.")
else:
    favorite_color = input("What is your favorite color? ")
    print(f"Your favorite color is {favorite_color}")

print(f"The command is {command}.")
print(f"The direction is {direction}.")
print(f"The subcode is {subcode}.")
print(f"The final argument is {argument}.")