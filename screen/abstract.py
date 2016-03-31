from abc import ABCMeta, abstractmethod
from constants import Keypad
import curses
import time


# abstract screen "interface"
#

class AbstractScreen:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def display_string(self, string):
        return

    @abstractmethod
    def clean_screen(self):
        return

# Abstract keypad "interface"
class AbstractKeypad:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.is_pressed = ""
        #pointer to screen

    @abstractmethod
    def key_pressed(self):
        pass

    @abstractmethod
    def stop_and_clean(self):
        pass

    def start_listening(self):
        refresh_rate = 20
        prev = ''
        while self.is_pressed <> Keypad.EXIT:
            char = self.key_pressed()
            self.is_pressed = char
            time.sleep(1.0/refresh_rate)
        self.stop_and_clean()
