from abc import ABCMeta, abstractmethod
from screen.abstract import *
from constants import Keypad
import time
import thread


# abstract class which defines abstract menu. Every menu and submenu should
# implement actions
#
class AbstractMenu:
    __metaclass__ = ABCMeta

    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screens = screen
        self.refresh_rate = 20
        self.temp_char = ""

    @abstractmethod
    def main_screen(self):
        return

    @abstractmethod
    def left_action(self):
        return

    @abstractmethod
    def right_action(self):
        return

    @abstractmethod
    def up_action(self):
        return

    @abstractmethod
    def down_action(self):
        return

    @abstractmethod
    def accept_action(self):
        return

    def display_string(self,message):
        for scr in self.screens:
            scr.display_string(message)

    def start(self):
        thread.start_new_thread(self.keypad.start_listening,())
        prev = ""
        while self.keypad.is_pressed <> Keypad.EXIT:
            char = self.keypad.is_pressed
            if char is not prev:
                if char == Keypad.LEFT:
                    self.left_action()
                elif char == Keypad.RIGHT:
                    self.right_action()
                elif char == Keypad.UP:
                    self.up_action()
                elif char == Keypad.DOWN:
                    self.down_action()
                elif char == Keypad.SELECT:
                    self.accept_action()
                prev = self.keypad.is_pressed
                time.sleep(0.3)

            else:
                self.main_screen()
            time.sleep(1.0/1.5)
