from abstract import AbstractMusicClient
from telnetlib import Telnet


class SpotifyClient(AbstractMusicClient):
    """ Simple client for spopd daemon.


    """

    def play(self):
        pass

    def stop(self):
        self.__execute_command("stop")

    def __init__(self):
        self.host = "localhost"
        self.port = 6602
        self.current_playlist = 10
        self.playlist = self.init_playlists()

    def get_current_song(self):
        status = self.__execute_command("status")
        artist = self.__get_status_index(5, status)
        title = self.__get_status_index(6, status)
        number = self.__get_status_index(4, status)
        return str(number) + ". " + title + " - " + artist

    def is_playing(self):
        if self.__execute_command("status").split(",")[0].split(":")[1].replace('"', '') == "playing":
            return True
        else:
            return False

    def get_current_time(self):
        time = float(self.__get_status_index(9))
        return "%02d:%02d" % ((time / 60), (time % 60))

    def next_track(self):
        self.__execute_command("next")

    def previous_track(self):
        self.__execute_command("prev")

    def play(self, playlist=None):
        if playlist is None:
            self.__execute_command("play")
        else:
            self.__execute_command("play " + self.current_playlist)

    def volume_up(self):
        pass

    def volume_down(self):
        pass

    def __execute_command(self, command):
        tel = Telnet(self.host, self.port)
        tel.write(command + "\n")
        tel.write("bye\n")
        temp = tel.read_all().split('\n')[1].replace("{", '').replace("}", '')
        tel.close()
        return temp

    def __get_status_index(self, index, status=None):
        """ Returns one of the following information according the given index:
        0 - status
        1 - repeat
        2  - shuffle
        3 - total_tracks
        4 - current_track
        5 - artist
        6 - title
        7 - album
        8 - duration
        9 - position
        10 - uri
        11 - popularity
        """
        if status is None:
            status = self.__execute_command("status")
        return status.split(',\"')[index].split(":")[1].replace('"', '')

    def exec_command(self, command):
        return self.__execute_command(command)

    def init_playlists(self):
        temp = self.__execute_command("ls").split('"index":')
        playlists = []
        for pl in temp:
            p = pl.split(',')
            if len(p) > 2:
                playlists.append((p[0] + ":" + p[2].split(":")[1]).replace('"',''))
        return playlists


client = SpotifyClient()

#print client.init_playlists()
#print len(client.init_playlists())
# print client.exec_command("play")
# print client.get_current_song()
