"""A trie tree."""


class Node(object):
    """Node or trie tree."""

    def __init__(self):
        """Init node."""
        self.prefix_count = 0
        self.children = {}


class TrieTree(object):
    """A trie tree written in python."""

    def __init__(self, iterable=None):
        """Init trie."""
        self.root = Node()
        self.size_count = 0
        if isinstance(iterable, (str, list, tuple)):
            for word in iterable:
                self.insert(word)

    def insert(self, word):
        """Insert into trie tree."""
        if not isinstance(word, str):
            raise ValueError('Argument must be string.')

        current_node = self.root

        # insert word in tree
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = Node()
            current_node = current_node.children[letter]
            current_node.prefix_count += 1

        # add ending charactor
        current_node.children['$'] = Node()

        # increment size count
        self.size_count += 1

    def contains(self, word):
        """Check if tree contains."""
        
        pass

    def size(self):
        """Check  of tree."""
        return self.size_count

    def remove(self, word):
        """Remove from tree."""
        self.size_count -= 1
