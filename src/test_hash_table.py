"""Tests for hash table."""
import pytest


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


def test_additive_hash(table):
    """Test additive hash."""
    assert isinstance(table._additive_hash('hello'), int)


def test_exor_hash(table):
    """Test exor hash."""
    assert isinstance(table._exor_hash('hello'), int)


def test_fnc_hash(table):
    """Test fnv hash."""
    assert isinstance(table._fnv_hash('hello'), int)


def test_set_add_table(table):
    """Test set method."""
    table.set('key', 5)
    assert 5 in table.buckets


def test_set_exor_table(exor_table):
    """Test set method with exor table."""
    exor_table.set('key', 5)
    assert 5 in exor_table.buckets


def test_set_fnv_table(fnv_table):
    """Test set method fvn table."""
    fnv_table.set('key', 5)
    assert 5 in fnv_table.buckets


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
