# The Dungeon of Golthar 25
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("You came up in the void. This is impossible.")
        exit(1)

class Engine(object):
    def  __init__(self, scene_map):
        self.game_map = scene_map
    
    def play(self):
        while True:
            self.game_map.opening_scene().enter()
            self.game_map.next_scene('')

class Death(Scene):
    def __init__(self):
        super().__init__()
        self.cause = 'You died.'

    def __init__(self, cause):
        super().__init__()
        self.cause = cause

    def enter(self):
        print(self.cause)
        print("--- GAME OVER ---")
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("""
            You awaken in the central corridor of the SS Goliath. Last you remember, something horrible broke out of its ice shell.
            Why did those scientists bring that commet fragment onboard? Why weren't more labs done?
            BANG!
            Your hear the monster howling and clawing at doors along the corridor. You need to get to the laster weapons armory
            but the labels on the doors are scatched off. Which door do you pick: left or right?
            """)

        door_choice = input("Door choice: ")
        if door_choice.lower() == "right":
            print("It looks liek the laser weapons armory inside!")
        else:
            print("The door opens and the monster stares at you. It raises it's claw-laden hand.")
            Death("You get your face clawed off").enter()


class LaserWeaponsArmory(Scene):
    def enter(self):
        print("""
            The laser room is dark but at least some of the weapons are active. Unfortunately, it's only the weapons between
            this room and the next room, holding the monster. You can try for the door, enter command 1, or command 2.
            """)
        laser_choice = input("What is your choice? [door, 1, or 2]")

        if laser_choice.lower() == "door":
            print("The door opens but the monster escapes from the side door. It attacks you from behind.")
            Death("Your body is ripped apart.").enter()
        elif laser_choice == "2":
            print("You start internal laser system. It fires at everything in the room, including you.")
            Death("You're obliterated by your own ship's weapons.").enter()
        else:
            print("The lasers open fire in the next room. The monster screams and runs away wounded.")
            print("You're able to escape through the door.")

class TheBridge(Scene):
    def enter(self):
        print("""
            You enter the bridge. 
            The view screen is dark and cracked. You hear the scratching of the monster in the ready room.
            Command is uncreachable.
            The dead crew lay fallen at their stations. One crew member, the Android known as Kevin, has a sheet of paper in his hands.
            The paper reads 00101 01010 11111 00001. It looks like he was attempting to enter a 6-digit code into the ship's control
            before succumbing to his wounds.
            You think that the code is key to getting out.
        """)

        key_code = input("Input in the 6-digit code: ")
        self.check_code(key_code)

    def check_code(self, code):
        if code == "510311":
            # you got through it.
            print(""" 
                The door to the escape pod room opens.
                The computer chimes. 'Command code accepted. Self destruct in 30 seconds.'
                You better get a move on!
                """)
        else: 
            print("The bridge is illuminated with red lights. The computer says, 'Code not accepted. Self destruct initiating.'")
            Death("You explode wtith the rest of the ship.").enter()


class EscapePod(Scene):
    def __init__(self):
        self.num_pods = 3
        self.correct_pod = randint(1, self.num_pods)

    def enter(self):
        print(f"""
            It's the pod room. Almost out.
            The computer voice overhead is counting down.
            There are {self.num_pods} open but only one may work.
            It's time to choose. Pods 1 through {self.num_pods}       
            """)
        pod_choice = int(input("What pod do you choose? "))
        self.check_pod(pod_choice)

    def check_pod(self, choice):
        if choice == self.correct_pod:
            print("""
                You were able to pick the correct working pod.
                The ship is now in your rear view as you watch
                the ship begin to explode. Starting from the engines.
                It appears that the enemy wasn't going to end without
                taking you with it.
                """)
            exit()
        elif choice <= self.num_pods and choice >= 1:
            death_scene_0 = Death("You entered an outhouse. Not a pod... KABOOOOM!!!")
            death_scene_0.enter()
        else:
            death_scene_1 = Death("The pod didn't work and you couldn't take off in time. KABOOOM!!")
            death_scene_1.enter()


class Map(object):
    scenes = ['CentralCorridor', 'LaserWeaponsArmory', 'Bridge', 'EscapePod', 'Death']
    current_scene_index = 0
    def __init__(self, start_scene):
        self.current_scene_index = 0

    def next_scene(self, scene_name):
        if scene_name != '':
            self.current_scene_index = self.scenes.index(scene_name)
        else:
            self.current_scene_index += 1

    def opening_scene(self):
        return self.get_scene(self.scenes[self.current_scene_index])

    def get_scene(self, scene_name):
        if scene_name == 'CentralCorridor':
            return CentralCorridor()
        elif scene_name == 'LaserWeaponsArmory':
            return LaserWeaponsArmory()
        elif scene_name == 'Bridge':
            return TheBridge()
        elif scene_name == 'EscapePod':
            return EscapePod()
        else:
            return Death('You didn\'t make it. You died.')

def main():
    a_map = Map('CentralCorridor')
    a_game = Engine(a_map)
    a_game.play()

main()