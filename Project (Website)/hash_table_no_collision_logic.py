# hash_table_no_collision_logic.py

class HashTableNoCollision:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # Each index can hold a single value

    def _hash(self, value):
        # Calculate the hash index using the ASCII sum % table size
        ascii_sum = sum(ord(char) for char in value)
        return ascii_sum % self.size

    def insert(self, value):
        index = self._hash(value)
        if self.table[index] is None:
            self.table[index] = value
            print(f"Inserted {value} at index {index}.")
        else:
            raise Exception(f"Collision detected: Value '{value}' cannot be inserted at index {index} because it's already occupied by '{self.table[index]}'.")

    def delete(self, value):
        index = self._hash(value)
        if self.table[index] == value:
            self.table[index] = None
            print(f"Deleted {value} from index {index}.")
        else:
            print(f"{value} not found at index {index}.")

    def search(self, value):
        index = self._hash(value)
        return self.table[index] == value

    def traverse(self):
        # Returns the entire hash table for rendering in HTML
        return [(i, value) for i, value in enumerate(self.table)]
