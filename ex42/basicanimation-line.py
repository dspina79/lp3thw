from os import system, name
import time

class LineAnimationEngine(object):

    def generateOscilation(self, max_width):
        interval = 0
        forward = True
        frames_sec = 1.000 / 60.000
        while True:
            if forward:
                while interval < max_width:
                    spacing = " " * interval
                    print(f"{spacing}*")
                    interval += 1
                    time.sleep(frames_sec)
                    self.clear_screen()
                forward = False
            if not forward:
                while interval > 0:
                    spacing = " " * interval
                    print(f"{spacing}*")
                    interval -= 1
                    time.sleep(frames_sec)
                    self.clear_screen()
                forward = True
        
    def clear_screen(self):
        """Clears the terminal screen of content"""
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


eng = LineAnimationEngine()
eng.generateOscilation(30)