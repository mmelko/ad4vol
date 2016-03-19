from screen.abstract import *
from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from constants import Keypad
import time


class AdafruitLCD(AbstractScreen):
    def __init__(self):
        self.lcd = Adafruit_CharLCDPlate()
        self.lcd.backlight(self.lcd.OFF)
        self.screen_position = 0;
        self.prev_song = ""

    def display_string(self, string):
        self.clean_screen()
        temp = string.split('\n')

        if len(temp) == 1:
            self.lcd.message(string)
            return

        song = temp[0]
        time = temp[1]
        if len(song) > 16 + self.screen_position:
            song = song[0 + self.screen_position:15 + self.screen_position]
            self.screen_position += 1
        else:
            self.screen_position = 0
        self.lcd.message(song + "\n     " + time)


    def clean_screen(self):
        self.lcd.clear()


class AdafruitKeypad(AbstractKeypad):
    def __init__(self):
        super(AdafruitKeypad, self).__init__()
        self.keypad = Adafruit_CharLCDPlate()
        self.keypad.backlight(self.keypad.OFF)
        # self.keypad.

    def stop_and_clean(self):
        pass

    def key_pressed(self):
        # self.main_screen()
        lcd = self.keypad
        # time.sleep(0.1)
        if lcd.buttonPressed(lcd.UP):
            return Keypad.UP
        elif lcd.buttonPressed(lcd.DOWN):
            return Keypad.DOWN
        elif lcd.buttonPressed(lcd.RIGHT):
            return Keypad.RIGHT
        elif lcd.buttonPressed(lcd.LEFT):
            return Keypad.LEFT
        elif lcd.buttonPressed(lcd.SELECT):
            return Keypad.SELECT
