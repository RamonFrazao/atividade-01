class Tv:

    def __init__(self, brand, size):
        self.__brand = brand
        self.__size = size

    def get_brand(self):
        return self.__brand

    def set_name(self, brand):
        self.__brand = brand

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
