from screen.abstract import AbstractScreen
from lib.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate


class AdafruitLCD(AbstractScreen):
    def __init__(self):
        self.lcd = Adafruit_CharLCDPlate()

    def display_string(self, string):
        self.lcd.message(string)

    def clean_screen(self):
        self.lcd.clear()
