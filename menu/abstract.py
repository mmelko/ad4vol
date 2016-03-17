from abc import ABCMeta, abstractmethod
from screen.abstract import *
from constants import Keypad


# abstract class which defines abstract menu. Every menu and submenu should
# implement actions
#
class AbstractMenu:
    __metaclass__ = ABCMeta

    def __init__(self, keypad, screen):
        self.keypad = keypad
        self.screen = screen

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

    def start(self):
        char = 0
        while char <> Keypad.EXIT:
            char = self.keypad.key_pressed()
            self.screen.clean_screen()
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
