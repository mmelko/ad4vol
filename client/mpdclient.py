from abstract import AbstractMusicClient
import mpd


class MPDClient(AbstractMusicClient):
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

    def is_playing(self):
        if self.getStatus('state') <> "stop":
            return True
        else:
            return False

    def get_current_time(self):
        self.connect()
        temp = self.client.status()['time'].split(":")[0]
        time = int(temp)
        self.client.disconnect()

        return "%02d:%02d" % ((time / 60), (time % 60))

    def connect(self):
        self.client.connect(self.host, self.port)

    def getStatus(self, thing):
        self.connect()
        res = self.client.status()[thing]
        self.client.disconnect()
        return res
