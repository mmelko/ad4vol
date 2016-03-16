from screen.dummy import DummyScreen
import time
import datetime



dummy_screen = DummyScreen()
refresh_rate = 20

while True:
    dummy_screen.clean_screen()
    dummy_screen.display_string(datetime.datetime.now().time())
    time.sleep(1.0/refresh_rate)


