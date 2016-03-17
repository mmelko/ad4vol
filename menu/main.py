from abstract import AbstractMenu
from screen.abstract import AbstractScreen


class HomeScreen(AbstractMenu):
  #  def __init__(self, keypad, screen):
  #      super(HomeScreen, self).__init__(keypad, screen)

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
