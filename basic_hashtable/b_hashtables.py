

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capcity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    return num % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))
    newPair = Pair(key, value)
    if hash_table.storage[index] is not None:
        print(f'Warning:  Collision occurred, overwriting "{hash_table.storage[index].key}": "{hash_table.storage[index].value}"" with "{newPair.key}": "{newPair.value}."')
    hash_table.storage[index] = newPair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] and hash_table.storage[index].key == key:
        hash_table.storage[index] = None
    else:
        print(f'Warning: Could not find key: "{key}" in the hash table.')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))
    if hash_table.storage[index] and hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    else:
        return None
        


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")
    hash_table_remove(ht, "seven")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
