from abstract import AbstractMenu
from screen.abstract import AbstractScreen
from client.mpdclient import MPDClient


class HomeScreen(AbstractMenu):
  #  def __init__(self, keypad, screen):
  #      super(HomeScreen, self).__init__(keypad, screen)
    def __init__(self,keypad,screen):
        super(HomeScreen,self).__init__(keypad,screen)
        self.client = MPDClient()

    def main_screen(self):
        self.screen.clean_screen()
        self.screen.display_string(self.client.get_current_song())

    def left_action(self):
        self.screen.display_string("Previous track")

    def right_action(self):
        self.screen.display_string("Next track")

    def up_action(self):
        self.screen.display_string("Volume UP")

    def down_action(self):
        self.screen.display_string("Volume Down")

    def accept_action(self):
        pass
