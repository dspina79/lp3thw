from os import system, name
import time

class LineAnimationEngine(object):
    def print_frame(self, interval, shift, frame_rate):
        spacing = " " * interval
        print(f"{spacing}*")
        interval += shift
        time.sleep(frame_rate)
        self.clear_screen()
        return interval

    def generateOscilation(self, max_width, frames_per_second):
        interval = 0
        forward = True
        frame_rate = 1.000 / float(frames_per_second)
        while True:
            if forward:
                while interval < max_width:
                    interval = self.print_frame(interval, 1, frame_rate)
                forward = False
            if not forward:
                while interval > 0:
                    interval = self.print_frame(interval, -1, frame_rate)
                forward = True
        
    def clear_screen(self):
        """Clears the terminal screen of content"""
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

def main():
    eng = LineAnimationEngine()
    eng.generateOscilation(30, 60)

main()