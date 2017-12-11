"""Tests for hash table."""
import pytest

f = open("/usr/share/dict/words", "r")
words = f.read().split('\n')


@pytest.fixture
def table():
    """Fixture for empty hash table."""
    from hash_table import HashTable
    table = HashTable(10, 'add')
    return table


@pytest.fixture
def exor_table():
    """Fixture for empty hash table."""
    from hash_table import HashTable
    table = HashTable(10, 'exor')
    return table


@pytest.fixture
def fnv_table():
    """Fixture for empty hash table."""
    from hash_table import HashTable
    table = HashTable(10, 'fnv')
    return table


@pytest.fixture
def large_fnv_table():
    """Fixture for empty hash table."""
    from hash_table import HashTable
    table = HashTable(2048, 'fnv')
    return table


def test_additive_hash(table):
    """Test additive hash."""
    assert isinstance(table._additive_hash('hello'), int)


def test_exor_hash(table):
    """Test exor hash."""
    assert isinstance(table._exor_hash('hello'), int)


def test_fnc_hash(table):
    """Test fnv hash."""
    assert isinstance(table._fnv_hash('hello'), int)


def test_set_key_not_string_error(table):
    """Test that an error is thrown when the key is not a string."""
    with pytest.raises(ValueError):
        table.set(5, 5)


def test_get_returns_val(table):
    """Test get returns val from table."""
    table.set('key', 5)
    assert table.get('key') == 5


def test_get_returns_val_exor(exor_table):
    """Test get for exor table."""
    exor_table.set('key', 5)
    assert exor_table.get('key') == 5


def test_get_returns_val_fnv(fnv_table):
    """Test fvn table get."""
    fnv_table.set('key', 5)
    assert fnv_table.get('key') == 5


def test_insert_more_vals_than_table_size(large_fnv_table):
    """Test returns vals even with collision."""

    for word in words:
        large_fnv_table.set(word, word)

    for word in words:
        assert large_fnv_table.get(word) == word


f.close()
