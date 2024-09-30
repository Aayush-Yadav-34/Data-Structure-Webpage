# hash_table_logic.py

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _ascii_hash_function(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, key):
        index = self._ascii_hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key):
        index = self._ascii_hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key):
        index = self._ascii_hash_function(key)
        return key in self.table[index]

    def display(self):
        return self.table

    def hash_code(self, key):
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum, ascii_sum % self.size
