from screen.dummy import DummyScreen, DummyKeypad
from menu.main import HomeScreen


client = HomeScreen(DummyKeypad(), DummyScreen())
refresh_rate = 20

client.start()