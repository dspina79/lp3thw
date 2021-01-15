# Branches and Functions


from sys import exit # used to perform exits in the game runtime

def gold_room():
    """The final chamber hall."""
    print("This room is full of gold. How much do you take?")
    choice  = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
    else:
        dead("You greedy bastard!")

def bear_room():
    """A room stage where a bear is present and ready to kill."""
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("Are you going to move the bear?")

    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
            break
        else:
            print("I got no idea what that means.")

def chtulu_room():
    """A room containing Cthulu which has the capability to resume to the start."""
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty.")
    else:
        chtulu_room()

def oubliette(): 
    """A little place of forgetting..."""
    dead("You fall into a pit with a large spike.")

def complete():
    """Ends the game so you're no longer in a loop."""
    print("And that's the game!")
    exit(0)

def dead(reason):
    """Ends the game under grim circumstances"""
    print(reason, "Good job!")
    exit(0)

def start():
    """Game initializer"""
    print("You are in a dark room.")
    print("There is a door to your right, left, and below you.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        chtulu_room()
    elif choice == "below":
        oubliette()
    else:
        dead("You stumble around until you starve.")


start()