# hash_table_chaining_logic.py

class HashTableChaining:
    def __init__(self):
        # Initialize the hash table with 10 empty buckets (for mod 10)
        self.table = [[] for _ in range(10)]

    def _hash(self, value):
        # Calculate the hash by summing the ASCII values of the characters in the string
        ascii_sum = sum(ord(char) for char in value)
        return ascii_sum % 10

    def insert(self, value):
        # Calculate the index using the new hash function
        index = self._hash(value)
        self.table[index].append(value)
        print(f"Inserted {value} into bucket {index}.")

    def delete(self, value):
        index = self._hash(value)
        if value in self.table[index]:
            self.table[index].remove(value)
            print(f"Deleted {value} from bucket {index}.")
        else:
            print(f"{value} not found in bucket {index}.")

    def search(self, value):
        index = self._hash(value)
        return value in self.table[index]

    def traverse(self):
        # Returns the entire hash table (for rendering in HTML)
        return [(i, bucket) for i, bucket in enumerate(self.table)]
