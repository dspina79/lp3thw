# New Decision Game

import random

print("""
The goal is to make 21 without going over.
Only 2 - 10 cards are provided.
""")

card1 = random.randrange(2, 10)
card2 = random.randrange(2, 10)

total = card1 + card2
print(f"You are dealt a {card1} and {card2} for a total of {total}.")
print(f"Print h to hit or Enter to end.")

action = input("> ")
lost = False

while action == "h" and not lost:
    if action == "h":
        card = random.randrange(2, 10)
        total += card
        print(f"You are dealt a {card} for a total of {total}.")
        if total == 21:
            print("You won!")
            action = "Won!"
        elif total > 21:
            print("Sorry, you lost.")
            lost = True
        else:
            print(f"Print h to hit or Enter to end.")
            action = input("> ")

print("Game Over")