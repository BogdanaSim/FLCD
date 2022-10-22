from collections import deque


class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__table = {}
        for i in range(0, self.__size):
            self.__table[i] = deque()

    def hash_function(self, value):
        s = 0
        for c in value:
            s += (ord(c) - 48)
        return s % self.__size

    def insert(self, value):

        key = self.hash_function(value)
        self.__table[key].append(value)

    def delete(self, value):
        key = self.hash_function(value)
        self.__table[key].remove(value)

    def search(self, value):
        key = self.hash_function(value)
        if value in self.__table[key]:
            return True
        return False

    def get_value_on_position(self, key, position):
        return self.__table[key][position]

    def get_index(self, value):
        key = self.hash_function(value)
        return self.__table[key].index(value)

    def __str__(self):
        text = ""
        for key in self.__table:
            text = text + str(key) + " -> { "
            for value in self.__table[key]:
                text = text + str(value) + " -> "
            text = text[:-3]
            if text[-1] == ">":
                text += " { "
            text += "}\n"
        return str(text)
