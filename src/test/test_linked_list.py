"""."""

import pytest
import random


def test_node_has_attributes():
    """."""
    from linked_list import Node
    n = Node(1, None)
    assert hasattr(n, 'data')


# def test_linked_list_pop_empty_raises_exception():
#     """."""
#     from linked_list import LinkedList
#     l = LinkedList()
#     with pytest.raises(IndexError):
#         l.pop()


# def test_linked_list_size_returns_none():
#     """."""
#     from linked_list import LinkedList
#     l = LinkedList
#     assert l.size == 0


# @pytest.mark.parametrize('n', range(100))
# def test_linked_list_size_returns_length(n):
#     """."""
#     from linked_list import LinkedList
#     l = LinkedList
#     for i in range(n):
#         l.push(i)
#     assert l.size == 1


# def test_linked_list_search_with_one_node_returns_node():
#     """."""
#     from linked_list import LinkedList
#     l = LinkedList
#     l.push(1)
#     assert l.search(0) is None


# @pytest.mark.parametrize('n', range(10))
# def test_linked_list_search_in_many_returns_proper_node(n):
#     """."""
#     from linked_list import LinkedList
#     l = LinkedList
#     for i in range(1, n + 1):
#         l.push(i)
#     search_me = random.randint(1, n)
#     assert l.search(search_me).data == search_me
