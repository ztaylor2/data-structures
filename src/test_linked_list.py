"""."""

import pytest


def test_node_has_attributes():
    """."""
    from linked_list import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')


def test_linked_list_has_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_last_value_is_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_two_last_value_is_next_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_removes_and_returns_head():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_linked_list_removes_and_returns_head_value():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    output = l.pop()
    assert output == 'potato'


def test_linked_list_pop_shifts_head_properly():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_returns_size_returns_list_length():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(10))
def test_linked_list_returns_size_returns_list_length_one(n):
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(10))
def test_linked_list_returns_size_returns_list_len_function(n):
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_with_one_node_returns_node():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search_one_returns_none():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


def test_linked_list_can_take_iterable():
    """."""
    from linked_list import LinkedList
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_display_with_one_node():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    assert l.display() == '(8)'


def test_display_with_mult_nodes():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    l.push(9)
    l.push(55)
    assert l.display() == '(55, 9, 8)'


def test_remove_linked_list_single():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    l.remove(8)
    assert l.display() == '()'


def test_remove_linked_list():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    l.push(9)
    l.push(10)
    l.remove(9)
    assert l.display() == '(10, 8)'


def test_remove_linked_list_empty():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        assert l.remove(8)


def test_print():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    l.push(9)
    l.push(10)
    l.remove(9)
    assert l.__str__() == '(10, 8)'


def test_len():
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(8)
    l.push(9)
    l.push(10)
    assert l.__len__() == 3
