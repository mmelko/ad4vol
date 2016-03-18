from screen.dummy import DummyScreen, DummyKeypad
from menu.main import HomeScreen
from screen.adafruit import AdafruitLCD, AdafruitKeypad


#client = HomeScreen(DummyKeypad(), DummyScreen())
lcd =  {DummyScreen()}
#lcd = DummyScreen()
keypad = AdafruitKeypad()
#keypad = DummyKeypad()
client = HomeScreen(keypad,lcd)
refresh_rate = 20

client.start()
