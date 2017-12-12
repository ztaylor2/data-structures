"""Test trie tree."""

import pytest


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
