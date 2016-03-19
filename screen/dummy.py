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
        self.clean_screen()
        sys.stdout.write(string+"\n")

    def clean_screen(self):
        os.system('clear')



class DummyKeypad(AbstractKeypad):

    def __init__(self):
        super(DummyKeypad,self).__init__()
        '''try:
            self.screen = curses.initscr()
            curses.cbreak()
            #curses.noecho()
        except:
      # In event of error, restore terminal to sane state.
            self.screen.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            traceback.print_exc()

        '''
    def key_pressed(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        #print "b;a b;a bla bla bal alb"

        #ch = self.screen.getch()

        #return self.which_key(str(unichr(ch)))
        return self.which_key(ch)

    def stop_and_clean(self):
        pass
        #curses.echo()
        #curses.nocbreak()
        #curses.endwin()

    def which_key(self, char):
        if char == 'w':
            return Keypad.UP
        elif char == 's':
            return Keypad.DOWN
        elif char == 'd':
            return Keypad.RIGHT
        elif char == 'a':
            return Keypad.LEFT
        elif char == "e":
            return Keypad.SELECT
            #press CTRL+C
        elif ord(char) == 3:
            return Keypad.EXIT
