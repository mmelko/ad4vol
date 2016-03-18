from abstract import AbstractMusicClient
import mpd

class MPDClient (AbstractMusicClient):

    def __init__(self):
        self.client = mpd.MPDClient()
        self.client.timeout = 10
        self.host = "localhost"
        self.port = 6600

    def get_current_song(self):
        self.connect()
        current = self.client.currentsong()
        artist = "None"
        title = "None"
        if 'artist' in current:
            artist = current['artist']

        if 'title' in current:
            title = current['title']
        self.client.disconnect()
        return artist + " - " + title



    def get_current_time(self):
        pass

    def connect(self):
        self.client.connect(self.host,self.port)
