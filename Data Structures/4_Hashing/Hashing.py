class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        return None

# Example usage
hash_table = HashTable(size=10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)

print(hash_table.search("apple"))  # Output: 5
print(hash_table.search("banana"))  # Output: 10
print(hash_table.search("cherry"))  # Output: None


##############################################


# Creating a hashmap
my_dict = {}  # or my_dict = dict()

# Adding key-value pairs
my_dict["apple"] = 5
my_dict["banana"] = 10
my_dict["cherry"] = 15

# Accessing values using keys
print("Value of 'apple':", my_dict["apple"])
print("Value of 'banana':", my_dict["banana"])

# Checking if a key exists
if "cherry" in my_dict:
    print("'cherry' exists in the hashmap")

# Deleting a key-value pair
del my_dict["apple"]

# Iterating through the hashmap
for key, value in my_dict.items():
    print(key, ":", value)

# Getting a default value for a non-existent key
nonexistent_value = my_dict.get("nonexistent_key", "Key not found")
print("Value for 'nonexistent_key':", nonexistent_value)
