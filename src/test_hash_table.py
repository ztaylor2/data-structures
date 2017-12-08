"""Tests for hash table."""


def test_additive_hash():
    """Test additive hash."""
    from hash_table import HashTable
    table = HashTable(10, 'add')
    assert isinstance(table._additive_hash('hello'), int)


def test_exor_hash():
    """Test exor hash."""
    from hash_table import HashTable
    table = HashTable(10, 'add')
    assert isinstance(table._exor_hash('hello'), int)


def test_fnc_hash():
    """Test fnv hash."""
    from hash_table import HashTable
    table = HashTable(10, 'add')
    assert isinstance(table._fnv_hash('hello'), int)
