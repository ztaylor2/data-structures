"""A trie tree."""


class Node(object):
    """Node or trie tree."""

    def __init__(self):
        """Init node."""
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

        # add ending charactor
        current_node.children['$'] = Node()

        # increment size count
        self.size_count += 1

    def contains(self, word):
        """Check if tree contains."""
        current_node = self.root

        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        if '$' not in current_node.children:
            return False

        return True

    def size(self):
        """Check  of tree."""
        return self.size_count

    def remove(self, word):
        """Remove from tree."""
        current_node = self.root

        try:
            for letter in word:
                current_node = current_node.children[letter]

            if '$' in current_node.children:
                current_node.children.pop('$', None)

            self.size_count -= 1

        except KeyError:
            raise KeyError('Word not in tree.')

    def traversal(self, start):
        """A depth first traversal of the trie tree."""
        if not isinstance(start, str):
            raise ValueError('Argument must be string.')

        # set start node
        current_node = self.root

        start_letter = ''
        # if start != '':
        for letter in start:
            if letter not in current_node.children:
                return
            current_node = current_node.children[letter]
            start_letter = letter

        return self._dfs(current_node, start_letter)

    def _dfs(self, current_node, letter):
        """Depth first search."""
        if letter != '' and letter != '$':
            yield letter
        for letter in current_node.children:
            for letter_to_yield in self._dfs(current_node.children[letter], letter):
                yield letter_to_yield



if __name__ == '__main__':
    tree = TrieTree()
    tree.insert('hello')
    tree.insert('hi')
    import pdb; pdb.set_trace()
    print(next(tree.traversal('')))
