from abstract import AbstractMusicClient
from telnetlib import Telnet

'''


'''


class SpotifyClient(AbstractMusicClient):
    def __init__(self):
        self.host = "localhost"
        self.port = 6602

    def get_current_song(self):
        status = self.__execute_command("status")
        artist = self.__get_status_index(5, status)
        title = self.__get_status_index(6, status)
        number = self.__get_status_index(4, status)
        return str(number) + ". " + title + " - " + artist

    def is_playing(self):
        if self.__execute_command("status").split(",")[0].split(":")[1] == "playing":
            return True
        else:
            return False

    def get_current_time(self):
        time = float(self.__get_status_index(9))
        return "%02d:%02d" % ((time / 60), (time % 60))

    def __execute_command(self, command):
        tel = Telnet(self.host, self.port)
        tel.write(command + "\n")
        tel.write("bye\n")
        temp = tel.read_all().split('\n')[1].replace('"', '').replace("{", '').replace("}", '')
        tel.close()
        return temp

    '''
    returns one of the following information according the given index:
    0 - status
    1 - repeat
    2 - shuffle
    3 - total_tracks
    4 - current_track
    5 - artist
    6 - title
    7 - album
    8 - duration
    9 - position
    10 - uri
    11 - popularity

    '''

    def __get_status_index(self, index, status=None):
        if status is None:
            return self.__execute_command("status").split(',')[index].split(":")[1]
        else:
            return status.split(',')[index].split(":")[1]
