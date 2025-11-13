class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == key:
                print("Key already exists!")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table is full!")
                return

        self.table[index] = key
        print(f"Key {key} inserted at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        print("Key not found")
        return None

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = "DELETED"
            print(f"Key {key} deleted")

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


# Example usage
ht = HashTable()
ht.insert(5)
ht.insert(15)
ht.insert(25)
ht.insert(7)

ht.display()

ht.search(15)
ht.delete(15)
ht.display()

ht.insert(35)
ht.display()
