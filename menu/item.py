from abc import ABCMeta, abstractmethod


class MenuItem:
    __metaclass__ = ABCMeta

    __name__ = "abstract"
    __submenu__ = ""

    @abstractmethod
    def performAction(self):
        pass
