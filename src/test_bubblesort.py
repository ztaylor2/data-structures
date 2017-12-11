"""Test bubblesort."""

import random


def test_bubblesort_sorts_list():
    """Test bubblesort sorts list of vals."""
    from bubblesort import bubblesort
    unsorted_list = [6, 4, 7, 9, 0, 2]
    assert bubblesort(unsorted_list) == [0, 2, 4, 6, 7, 9]


def test_bubblesort_on_long_list():
    """Test bubblesort on very long list."""
    from bubblesort import bubblesort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = bubblesort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
