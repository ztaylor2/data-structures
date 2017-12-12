"""Test trie tree."""

import random
import pytest

f = open("/usr/share/dict/words", "r")
words = f.read().split('\n')


@pytest.fixture
def tree():
    """Empty tree fixture."""
    from trie import TrieTree
    tree = TrieTree()
    return tree


def test_tree_inits(tree):
    """Test that the tree has node on init."""
    assert isinstance(tree.root, object)


def test_insert_increases_size(tree):
    """Test that the insert method increases the size."""
    tree.insert('hello')
    tree.insert('hi')
    assert tree.size() == 2


def test_remove_decreases_size(tree):
    """Test that the remove function decrements the size."""
    tree.insert('hello')
    tree.insert('hi')
    tree.insert('help')
    tree.remove('help')
    tree.remove('hi')
    assert tree.size() == 1


def test_insert_adds_word(tree):
    """Test that the insert method adds a word and ending charactor."""
    tree.insert('hello')
    assert tree.root.children['h']
    assert tree.root.children['h'].children['e']
    assert tree.root.children['h'].children['e'].children['l']
    assert tree.root.children['h'].children['e'].children['l'].children['l']
    assert tree.root.children['h'].children['e'].children['l'].children['l'].children['o']
    assert tree.root.children['h'].children['e'].children['l'].children['l'].children['o'].children['$']


def test_insert_adds_two_words_correctly(tree):
    """Test that insert adds two words correctly."""
    tree.insert('hi')
    tree.insert('ho')
    assert tree.root.children['h']
    assert tree.root.children['h'].children['o']
    assert tree.root.children['h'].children['i']
    assert tree.root.children['h'].children['o'].children['$']
    assert tree.root.children['h'].children['i'].children['$']


def test_contains_retuirns_true(tree):
    """Test that contains returns true with one word."""
    tree.insert('hi')
    assert tree.contains('hi')


def test_containes_returns_false(tree):
    """Test that contanes returns false if word not in."""
    assert not tree.contains('hi')


def test_contains_returns_correct_many_vals(tree):
    """Test contains returns true with many values."""
    tree.insert('hi')
    tree.insert('hello')
    tree.insert('help')
    tree.insert('no')
    assert tree.contains('hi')
    assert tree.contains('hello')
    assert tree.contains('help')
    assert tree.contains('no')
    assert not tree.contains('hiiii')
    assert not tree.contains('not')
    assert not tree.contains('bla')


def test_size(tree):
    """Test size method works."""
    rand_word_list = []
    rand_words_to_delete = []

    for i in range(50):
        rand_word_list.append(words[random.randint(0, len(words) - 1)])

    for word in rand_word_list:
        delete_probability = random.randint(0, 1)
        if delete_probability == 1:
            rand_words_to_delete.append(word)
        tree.insert(word)

    assert tree.size() == 50

    for word in rand_words_to_delete:
        tree.remove(word)

    assert tree.size() == 50 - len(rand_words_to_delete)


def test_size_zero(tree):
    """Test size is zero when empty."""
    assert tree.size() == 0


def test_remove_removes_word(tree):
    """Test that remove removes a word."""
    tree.insert('hi')
    assert tree.contains('hi')
    tree.remove('hi')
    assert not tree.contains('hi')


def test_remove_removes_many_words(tree):
    """Test remove removes many words."""
    rand_word_list = []
    rand_words_to_delete = []

    for i in range(50):
        rand_word_list.append(words[random.randint(0, len(words) - 1)])

    for word in rand_word_list:
        delete_probability = random.randint(0, 1)
        if delete_probability == 1:
            rand_words_to_delete.append(word)
        tree.insert(word)

    for word in rand_words_to_delete:
        tree.remove(word)
        assert not tree.contains(word)


def test_insert_remove_insert_remove(tree):
    """Test insert then remove insert etc."""
    for i in range(5):
        tree.insert('hi')
        assert tree.contains('hi')
        tree.remove('hi')
        assert not tree.contains('hi')


def test_remove_raises_error_if_not_in_tree(tree):
    """Test that remove throws an error if word not in tree."""
    with pytest.raises(KeyError):
        tree.remove('hi')


def test_traversal_when_not_string_raises_error(tree):
    """Test traversal when not string raises error."""
    with pytest.raises(ValueError):
        tree.traversal(5)


def test_traversal(tree):
    """Test traversal."""
    tree.insert('hello')
    traversal = tree.traversal('')
    assert next(traversal) == 'h'
    assert next(traversal) == 'e'
    assert next(traversal) == 'l'
    assert next(traversal) == 'l'
    assert next(traversal) == 'o'

f.close()
