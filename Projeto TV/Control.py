import Tv


class Control (Tv.Tv):

    def __init__ (self, brand, size):
        super ().__init__ (brand, size)
        self.__connect = False
        self.__channel = 1
        self.__sound = 50

    def get_connect(self):
        return self.__connect

    def set_connect(self, connect):
        self.__connect = connect

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel):
        self.__channel = channel

    def get_sound(self):
        return self.__sound

    def set_sound(self, sound):
        self.__sound = sound
