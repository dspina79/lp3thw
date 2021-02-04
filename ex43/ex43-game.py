# The Dungeon of Golthar 25
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def  __init__(self, scene_map):
        pass
    
    def play(self):
        pass

class Death(Scene):
    def __init__(self, cause):
        super().__init__()
        self.cause = cause

    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponsArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def __init__(self):
        num_pods = 3
        correct_pod = randint(1, num_pods)

    def enter(self):
        print(f"""
            It's the pod room. Almost out.
            The computer voice overhead is counting down.
            There are {self.num_pods} open but only one may work.
            It's time to choose. Pods 1 through {self.num_pods}       
            """)
        pod_choice = int(input("What pod do you choose? "))
        check_pod(pod_choice)

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
    def __init__(self, start_scene):
        self.scene = opening_scene

    def next_scene(self, scene_name):
        self.scene = get_scene(scene_name)

    def opening_scene(self):
        return CentralCorridor()

    def get_scene(self, scene_name):
        pass

def main():
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()

main()