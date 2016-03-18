from screen.abstract import *
from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from constants import Keypad
import time


class AdafruitLCD(AbstractScreen):
    def __init__(self):
        self.lcd = Adafruit_CharLCDPlate()
        self.lcd.backlight(self.lcd.OFF)


    def display_string(self, string):
        self.clean_screen()
        self.lcd.message(string)

    def clean_screen(self):
        self.lcd.clear()

class AdafruitKeypad(AbstractKeypad):
    def __init__(self):
        super(AdafruitKeypad,self).__init__()
        self.keypad = Adafruit_CharLCDPlate()
        self.keypad.backlight(self.keypad.OFF)

    def stop_and_clean(self):
        pass

    def key_pressed(self):
        #self.main_screen()
        lcd = self.keypad
        #time.sleep(0.1)
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
