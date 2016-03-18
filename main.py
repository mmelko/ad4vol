from screen.dummy import DummyScreen, DummyKeypad
from menu.main import HomeScreen
from screen.adafruit import AdafruitLCD


client = HomeScreen(DummyKeypad(), DummyScreen())
#client = HomeScreen(DummyKeypad(), AdafruitLCD())
refresh_rate = 20

client.start()
