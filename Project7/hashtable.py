"""
Implemented by: Yash Vesikar and Brandon Field
"""


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other):
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def __len__(self):
        """
        don't edit this plz
        Getter for size
        :return: size
        """
        return self.size

    ########## EDIT BELOW ##########

    def __setitem__(self, key, value):
        """
        Creates a node in the hash table that has the key and value that are passed in as parameters
        :param key: key to insert
        :param value: values to insert
        :return: None
        """
        self._insert(key, value)

    def __getitem__(self, key):
        """
        Gets the item with the key denoted by the item parameter
        :param key: key to search
        :return: return values associated with the key
        """
        result = self._get(key)
        if result is None:
            raise KeyError
        return result.value

    def __delitem__(self, key):
        """
        Deletes the node that has the value denoted by the key parameter
        :param key: key to delete
        :return: None
        """
        self._delete(key)
        # raise KeyError

    def __contains__(self, key):
        """
        Determines if a node with the key denoted by the item parameter exists in the table
        :param key: key to check
        :return: Boolean
        """
        index = self.hash(key)
        if self.table[index] is None:
            return False
        if self.table[index].key == key:
            return True
        else:
            return False

    def hash(self, key, inserting=False):
        """
        Given a key string return an index in the hash table.
        :param key: key to hash
        :param inserting: whether inserting or searching
        :return: possible index
        """
        i = 0
        hash1_i = self._hash_1(key)
        hash2_i = self._hash_2(key)
        while i < self.capacity:
            index = (hash1_i + i * hash2_i) % self.capacity
            if self.table[index] is None:
                return index
            elif self.table[index].key is None:
                if self.table[index].deleted == inserting:
                    return index
            elif self.table[index].key == key:
                return index
            i += 1

    def _insert(self, key, value):
        """
        Use the key and value parameters to add a HashNode to the hash table
        :param key: key to insert
        :param value: value to insert
        :return: None
        """
        new_node = HashNode(key, value)
        index = self.hash(key, True)
        self.table[index] = new_node
        self.size += 1
        if self.size >= self.capacity / 2:
            self._grow()


    def _get(self, key):
        """
        Find the HashNode with the given key in the hash table
        :param key: key to find node
        :return: node
        """
        index = self.hash(key)
        if self.table[index] is None:
            return None
        result = self.table[index]
        return result

    def _delete(self, key):
        """
        Removes the HashNode with the given key from the hash table
        :param key: key to find node
        :return: none
        """
        i = 0
        while i < self.capacity:
            index = self.hash(key)
            if self.table[index] is not None:
                self.table[index].key = None
                self.table[index].value = None
                self.table[index].deleted = True
                self.size -= 1
                break
            i += 1

    def _grow(self):
        """
        Double the capacity of the existing hash table
        :return: none
        """
        new_cap = self.capacity * 2
        old_cap = self.capacity
        new_table = [None] * new_cap
        old_table = self.table
        i = 0
        while HashTable.primes[i] <= new_cap:
            i += 1
        self.prime_index = i - 1

        self.capacity = new_cap
        self.table = new_table
        i = 0
        while i < old_cap:
            if old_table[i] is not None:
                if old_table[i].deleted is False:
                    hash1_index = self.hash(old_table[i].key, True)
                    self.table[hash1_index] = old_table[i]
            i += 1

    def update(self, pairs=[]):
        """
        Updates the hash table using an iterable of key value pairs
        :param pairs: pairs of tuples to update
        :return: none
        """
        for i in pairs:
            self.__setitem__(i[0], i[1])

    def setdefault(self, key, default=None):
        """
        Sets the default value for the key denoted by the key parameter using the default parameter
        :param key: key to find
        :param default: values to set
        :return: If the key exists in the table already, return the key's value, otherwise return the default parameter
        """
        if self.__contains__(key) is False:
            self.__setitem__(key, default)
            return default
        else:
            return self.__getitem__(key)

    def keys(self):
        """
        Returns a generator object that contains all of the keys in the table
        :return:generator object of keys
        """
        for i in self.table:
            if i is not None:
                if i.key is not None:
                    yield i.key

    def values(self):
        """
        Returns a generator object that contains all of the values in the table
        :return: generator object of values
        """
        for i in self.table:
            if i is not None:
                if i.value is not None:
                    yield i.value

    def items(self):
        """
        Returns a generator object that contains all of the keys and values in the table
        :return: generator object of tuple holds keys and values
        """
        for i in self.table:
            if i is not None:
                if i.key is not None:
                    if i.value is not None:
                        yield i.key, i.value

    def clear(self):
        """
        Should clear the table of HashNodes completely, in essence a reset of the table
        :return: None
        """
        new_table = [None] * self.capacity
        self.table = new_table
        self.size = 0

def hurdles(grid):
    """
    Given a grid that denotes a grid of hurdles, determine the minimum number of hurdles you will need to jump over to win the race
    :param grid: nested list
    :return: an integer representing the minimum number of hurdles that you must cross
    """
    sum = 0
    for i in grid[0]:
        sum += i
    table = HashTable(sum - 1)
    for eachNode in range(0, sum - 1):
        string = str(eachNode)
        table[string] = 0

    for i in range(0, len(grid)):
        line = 1
        check = 0
        j = 0
        while line < sum:
            check += grid[i][j]
            if check == line:
                line += 1
                j += 1
            elif check != line:
                inc = table[str(line - 1)] + 1
                table[str(line - 1)] = inc
                check -= grid[i][j]
                line += 1

    min = len(grid)
    values = table.values()
    for i in values:
        if i < min:
            min = i
    return min



