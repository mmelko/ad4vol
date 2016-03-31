from abstract import AbstractMenu
from screen.abstract import AbstractScreen
from client.mpdclient import MPDClient
from client.spotifyclient import SpotifyClient


class HomeScreen(AbstractMenu):
    #  def __init__(self, keypad, screen):
    #      super(HomeScreen, self).__init__(keypad, screen)
    def __init__(self, keypad, screen):
        super(HomeScreen, self).__init__(keypad, screen)
        self.clients = dict()
        self.clients['mpd'] = MPDClient()
        self.clients['spotify'] = SpotifyClient()
        self.active_client = "mpd"

          #  [MPDClient(), SpotifyClient()]

    def main_screen(self):
        client = self.__get_active_client()
        if client.is_playing() is True:
            self.display_string(client.get_current_song() + "\n" + client.get_current_time())
        else:
            self.display_string("Stopped")

    def __get_active_client(self):
        for name,client in self.clients.iteritems():
            if client.is_playing() is True:
                return client;
        return self.clients[self.active_client]

    def left_action(self):
        self.display_string("Previous track")
        self.__get_active_client().previous_track()

    def right_action(self):
        self.display_string("Next track")
        self.__get_active_client().next_track()

    def up_action(self):

        self.display_string("Spotify activated")
        self.active_client = 'spotify'

    def down_action(self):
        self.display_string("MPD activated")
        self.active_client = 'mpd'

    def accept_action(self):
        client = self.__get_active_client()
        if client.is_playing() is True:
            client.stop()
        else:
            client.play()
