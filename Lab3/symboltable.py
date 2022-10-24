from hashtable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hash_table = HashTable(size)

    def insert(self, value):
        self.__hash_table.insert(value)

    def delete(self, value):
        self.__hash_table.delete(value)

    def search(self, value):
        return self.__hash_table.search(value)

    def get_value_on_position(self, key, position):
        return self.__hash_table.get_value_on_position(key, position)

    def get_index(self, value):
        return self.__hash_table.get_index(value)

    def get_position(self, value):
        return self.__hash_table.get_position(value)

    def __str__(self):
        return str(self.__hash_table)
