from screen.abstract import *
from constants import Keypad
import sys
import tty
import termios
import os

'''
@Author mmelko
Dummy screen implementation, mainly for testing purposes. Dummy screen shows
 information directly to console output '''


class DummyScreen(AbstractScreen):
    def display_string(self, string):
        print string

    def clean_screen(self):
        os.system('clear')


class DummyKeypad(AbstractKeypad):
    def key_pressed(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print ord(ch)

        return self.which_key(ch)

    def which_key(self, ch_number):
        if ch_number == '\x1b[A':
            return Keypad.UP
        elif ch_number == '\x1b[B':
            return Keypad.DOWN
        elif ch_number == '\x1b[C':
            return Keypad.RIGHT
        elif ch_number == '\x1b[D':
            return Keypad.LEFT
        else:
            return Keypad.EXIT
