"""Hash table in python."""

from linked_list import LinkedList


class HashTable(object):
    """A hash table in python."""

    def __init__(self, size, hash_func):
        """Init hash table."""
        self.size = size
        self.hash_func = hash_func
        self.buckets = [LinkedList() for i in range(size)]
        if self.hash_func != 'add' and self.hash_func != 'exor' and self.hash_func != 'fnv':
            raise ValueError('Valid hash_func vals include add, exor, and fnv')

    def get(self, key):
        """Get a value from the table."""
        if self.hash_func == 'add':
            hashed_key = self._additive_hash(key)
        if self.hash_func == 'exor':
            hashed_key = self._exor_hash(key)
        if self.hash_func == 'fnv':
            hashed_key = self._fnv_hash(key)

        mapped_key = hashed_key % self.size

        current_node = self.buckets[mapped_key].head

        while current_node:
            if current_node.data == key:
                return current_node.next.data

            current_node = current_node.next

        raise KeyError("Key not in HashTable")

        # store key and val in linked list as toople then access val with key

    def set(self, key, val):
        """Set a value in the table."""
        if isinstance(key, str):

            if self.hash_func == 'add':
                hashed_key = self._additive_hash(key)
            if self.hash_func == 'exor':
                hashed_key = self._exor_hash(key)
            if self.hash_func == 'fnv':
                hashed_key = self._fnv_hash(key)

            mapped_key = hashed_key % self.size

            # this linked list will insert this tuple as seperate nodes
            self.buckets[mapped_key].push((val, key))

        else:
            raise ValueError('Keys should be strings.')

    def _additive_hash(self, key):
        """Hash a value with additive hash."""
        hashed_key = 0
        for val in key:
            hashed_key += ord(val)

        return hashed_key

    def _exor_hash(self, key):
        """Hash a value with exor hash."""
        hashed_key = 0
        for val in key:
            hashed_key ^= ord(val)

        return hashed_key

    def _fnv_hash(self, key):
        """FNV hashing function."""
        h = 2166136261
        for char in key:
            h = (h * 16777619) ^ ord(char)

        return h
