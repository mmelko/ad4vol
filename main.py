from screen.dummy import DummyScreen, DummyKeypad
from menu.main import HomeScreen
from screen.adafruit import AdafruitLCD, AdafruitKeypad
import os, sys

fpid = os.fork()
if fpid!=0:
#client = HomeScreen(DummyKeypad(), DummyScreen())
    print fpid
    lcd =  {AdafruitLCD()}
    #lcd = DummyScreen()
    keypad = AdafruitKeypad()
    #keypad = DummyKeypad()
    client = HomeScreen(keypad,lcd)
    refresh_rate = 20
    client.start()
    sys.exit(0)
