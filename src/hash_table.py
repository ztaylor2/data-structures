"""Hash table in python."""


class HashTable(object):
    """A hash table in python."""

    def __init__(self, size, hash_func):
        """Init hash table."""
        self.size = size
        self.hash_func = hash_func
        self.buckets = []
        if self.hash_func != 'add' or self.hash_func != 'exor' or self.hash_func != 'fnv':
            raise ValueError('Valid hash_func vals include add, exor, and fnv')

    def get(self, val):
        """Get a value from the table."""
        pass

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

            self.buckets[mapped_key] = val

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

    def _map_index(self, hash):
        """Map a hashed value to an index."""
        pass
