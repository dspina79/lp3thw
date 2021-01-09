# Guessing game

import random

def game():
    random.seed(18238)
    number_of_attempts_left = 5
    magic_number = random.randrange(1,30)
    game_won = False

    while number_of_attempts_left > 0 and not game_won:
        
        guess = int(input("Select a number between 1 and 30: "))
        if guess == magic_number:
            print("You won!")
            game_won = True
        elif guess > magic_number:
            print("Too high. Try again")
        else: 
            print("Too low. Try again.")
        
        number_of_attempts_left -= 1
    
    if game_won:
        print("Congratulations on your victory.")
    else:
        print(f"Sorry, you ran out of attempts. The correct answer was {magic_number}.")
    
    print("Would you like to play again? If so type Y at the prompt.")
    play_again = input("> ")

    if play_again == "Y":
        game()

# start it
game()