# The Secondary Dungeon

from sys import exit

def level1(player_name):
    print("\n\n---LEVEL 1---")
    print("You encounter a scout soldier.")
    print("Attack with what?")
    print("1. Spell of Ackemon\n2.Mace\n3.Bastard Sword\n4.Arrows")
    attack = input("> ")
    if attack in "1234":
        print("The scout is defeated.")
        level2(player_name)
    else:
        print("You failed to fight. You were killed.")
        game_over(False, player_name)
    

def level2(player_name):
    print("\n\n---LEVEL 2---")
    slime_molds = 3
    num_attacks = 0
    while slime_molds > 0 and num_attacks < 6:
        print(f"Before you stands {slime_molds} slime molds.")
        print("How will you attack?")
        print("1. Spell of Ackemon\n2.Mace\n3.Bastard Sword\n4.Arrows")
        attack = input("> ")
        num_attacks = num_attacks + 1
        if attack in "12":
            print("Ha! You kill a slime mold!")
            slime_molds = slime_molds - 1
        elif attack == "4":
            print("The arrow bounces back and kills you.")
            game_over(False, player_name)
        else:
            print("The slime molds are not damaged.")
        
    if slime_molds == 0:
        print("All of the slime molds are defeated.")
        level3(player_name)
    else:
        print("The remaining slime molds overcome you. You die.")
        game_over(False, player_name)
    

def level3(player_name):
    print("\n\n---LEVEL 3---")
    elites = 2
    elite_life = 2
    num_attacks = 0
    while elites > 0 and num_attacks < 4:
        print(f"Before you stands {elites} elite soldiers")
        print("How will you attack?")
        print("1. Spell of Ackemon\n2.Mace\n3.Bastard Sword\n4.Arrows")
        attack = input("> ")
        num_attacks = num_attacks + 1
        if attack == "1":
            print("The Spell of Ackemon bounces off their armor. You die.")
            game_over(False, player_name)
        else:
            print("You successfully hit one of the elites and damage them.")
            elite_life = elite_life - 1
            if elite_life == 0:
                elites = elites - 1
                elite_life = 2
                print("One has fallen!")
    
    if elites == 0:
        print("All of the elite soldiers are defeated.")
        print(f"""
            Before the last one falls, it cries out, \"Our Master knows your name, {player_name}!\"
            Then dies.
        """)
        boss(player_name)
    else:
        print("The elites overcome you. You die.")
        game_over(False, player_name)


def boss(player_name):
    print("\n\n---BOSS BATTLE---")
    """Attempt to defeat the boss."""

    print(f"""
        The epic chamber is occupied by one figure.
        The evil MASTER LORD HOVASH.
        He holds the ebony blade and the fist of fire.
        \"You shall not defeat me, {player_name}!\"
    """)
    print("How will you attack?")
    print("1. Spell of Ackemon\n2.Mace\n3.Bastard Sword\n4.Arrows\n5.The Anti-Evil Equation")
    attack = input("> ")
    if attack == "5":
        print("Hovath falls dead. You have defeated him.")
        game_over(True, player_name)
    else:
        print("Hovath laughs as the attack bounces off of him and kills you.")
        game_over(False, player_name)

def game_over(win, player_name):
    """The end of the game dependent on the win or loss"""
    if win:
        print(f"Congratulations, {player_name}, you won!")
        print("Play again soon.")
    else: 
        print("Epic Fail.")
        print("---GAME OVER---")
    exit(0)

def start():
    print("Welcome traveler. What is your name?")
    player_name = input("> ")
    level1(player_name)    

start()