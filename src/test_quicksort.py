"""Test quicksort."""

import random


def test_quicksort_with_lots_of_random_lists():
    """Test quicksort with lots of random lists."""
    from quicksort import quicksort

    # test on 100 lists
    for i in range(100):
        # generate random length of list
        list_length = random.randint(0, 100)
        unsorted_list = []
        for x in range(list_length):
            # generate random numbers for each item in list and append to list
            unsorted_list.append(random.randint(0, 100))

        # test that list is sorted
        assert quicksort(unsorted_list) == sorted(unsorted_list)
