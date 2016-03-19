from abc import ABCMeta, abstractmethod


# abstract screen "interface"
#

class AbstractMusicClient:
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
