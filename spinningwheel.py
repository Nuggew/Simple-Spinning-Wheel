import sys
import time
import threading
import colorist
from colorama import just_fix_windows_console
import numpy as np

class SpinningWheel:
    def __init__(self, msg="", color=(255,255,255)):
        self.msg = msg
        self.color = colorist.ColorRGB(color[0],color[1],color[2])
        just_fix_windows_console()

    def spinning_cursor(self):
        while True:
            for cursor in '|/-\\':
                yield cursor

    def spin(self):
        spinner = self.spinning_cursor()
        while self.running:
            sys.stdout.write(f"{self.color} {next(spinner)} {self.msg}{colorist.Color.OFF}")
            sys.stdout.flush()
            time.sleep(0.1)
            for _ in f"{self.color}@ {self.msg}{colorist.Color.OFF}":
                sys.stdout.write('\b')

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.spin)
        thread.start()

    def stop(self):
        self.running = False

class ProgressBar:
    def __init__(self, value=0, showPercentage=False, msg=""):
        self.showPercentage = showPercentage
        if msg != "":
            self.msg = f" - {msg}"
        else:
            self.msg = ""
        self.value = value
        just_fix_windows_console()

    def update(self):
        complete = ""
        incomplete = ""

        percentage = int(self.value * 20)
        percentageStr = ""

        if self.showPercentage:
            percentageStr = f" {int(self.value * 100)}%"

        for _ in np.arange(percentage):
            complete += "█"

        for _ in np.arange(20 - percentage):
            incomplete += "░"

        for _ in f"[@@@@@@@@@@@@@@@@@@@@]{percentageStr}{self.msg}":
            sys.stdout.write('\b')
        sys.stdout.write(f"[{colorist.Color.GREEN}{complete}{colorist.Color.RED}{incomplete}{colorist.Color.OFF}]{percentageStr}{self.msg}")
        sys.stdout.flush()

    def show(self):
        self.update()

    def set(self, value):
        self.value = value
        self.update()