from abc import ABCMeta, abstractmethod


# abstract screen "interface"
#

class AbstractMusicClient:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_current_song(self):
        pass

    @abstractmethod
    def get_current_time(self):
        pass

    @abstractmethod
    def is_playing(self):
        pass

    @abstractmethod
    def next_track(self):
        pass

    @abstractmethod
    def previous_track(self):
        pass
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass
