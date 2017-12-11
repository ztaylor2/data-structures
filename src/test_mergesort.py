"""Test merge sort."""


import random


def test_mergesort_sorts_list():
    """Test mergesort sorts list of vals."""
    from mergesort import mergesort
    unsorted_list = [6, 4, 7, 9, 0, 2]
    assert mergesort(unsorted_list) == [0, 2, 4, 6, 7, 9]


def test_mergesort_on_long_list():
    """Test mergesort on very long list."""
    from mergesort import mergesort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = mergesort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
