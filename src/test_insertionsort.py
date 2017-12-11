"""Test insertion sort."""

import random


def test_insertionsort_sorts_list():
    """Test insertionsort sorts list of vals."""
    from insertionsort import insertionsort
    unsorted_list = [6, 4, 7, 9, 0, 2]
    assert insertionsort(unsorted_list) == [0, 2, 4, 6, 7, 9]


def test_insertionsort_on_long_list():
    """Test insertionsort on very long list."""
    from insertionsort import insertionsort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = insertionsort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
