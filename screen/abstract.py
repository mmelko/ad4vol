from abc import ABCMeta, abstractmethod


# abstract screen "interface"
#

class AbstractScreen:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def display_string(self, string):
        return

    @abstractmethod
    def clean_screen(self):
        return


# Abstract keypad "interface"
class AbstractKeypad:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def key_pressed(self):
        pass
