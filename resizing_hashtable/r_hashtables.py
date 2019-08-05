import copy

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.initialCapacity = capacity
        self.storage = [None] * capacity
        self.items = 0
        self.max_load = 0.7
        self.min_load = 0.2
    
    def __repr__(self):
        return f"I am a HashTable with capacity for {self.capacity} items, and currently hold {self.items} items"


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    return num % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))
    newPair = LinkedPair(key, value)
    hash_table.items += 1
    # if nothing in that bucket, drop our new LinkedPair there
    if hash_table.storage[index] is None:
        hash_table.storage[index] = newPair
    # if we have a collision
    else:
        # traverse linked list stopping either at end of list or if we find that the key already exists
        current = hash_table.storage[index]
        while current.next and current.key != key:
            current = current.next
        # current is now the last Pair or the pair with the matching key
        if current.key != key:
            current.next = newPair
        else:
            current.value = value
        

    # resize up if load factor over 0.7
    load = hash_table.items / hash_table.capacity
    if load > hash_table.max_load:
        # print(f'growing hash table.  {hash_table.items} items, {hash_table.capacity} capacity, load is {load}')
        hash_table_resize(hash_table, 'grow')
        # print(f'load is now {hash_table.items / hash_table.capacity}')


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current = hash_table.storage[index]
    prev = None

    # traverse LL getting us to the end or stopping at a Pair with the same key
    while current and current.key != key:
        prev = current
        current = current.next
    
    if current is None:
        print(f"Warning: The key {key} was not found in the hash table")
    else:
        hash_table.items -= 1
        # if it's first element in LL, set the head to the 2nd element
        if prev is None:
            hash_table.storage[index] = current.next
        # if it's somewhere in middle, remove the pair by updating prev -> next pointer
        else:
            prev.next = current.next
    
    # if load factor below 0.2, shrink hash table (only if we're over original size)
    load = hash_table.items / hash_table.capacity
    if load < hash_table.min_load and hash_table.capacity > hash_table.initialCapacity:
        hash_table_resize(hash_table, 'shrink')

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))
    current = hash_table.storage[index]

    if current is None:
        return None

    while current.key != key and current.next:
        current = current.next
    
    if current.key == key:
        return current.value
    
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table, direction):
    temp = copy.deepcopy(hash_table.storage)

    if direction == 'grow':
        hash_table.capacity *= 2
    if direction == 'shrink':
        hash_table.capacity //= 2
    hash_table.storage = [None] * hash_table.capacity
    hash_table.items = 0

    for i in range(len(temp)):
        current = temp[i]
        while current:
            hash_table_insert(hash_table, current.key, current.value)
            current = current.next

def Testing():
    ht = HashTable(1)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    hash_table_insert(ht, "line_4", "Linked list saves the day!")

    # hash_table_remove(ht, "line_2")
    # hash_table_remove(ht, "line_3")
    # hash_table_remove(ht, "line_4")
    # hash_table_remove(ht, "line_1")
    
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

Testing()
