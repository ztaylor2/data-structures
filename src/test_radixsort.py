"""Test radix sort."""

import random


def test_stringify_nums():
    """."""
    from radixsort import stringify_nums
    nums = [1, 2, 3, 4, 5]
    stringified_nums = stringify_nums(nums)
    assert stringified_nums == ['1', '2', '3', '4', '5']


def test_while_condition():
    """."""
    from radixsort import while_condition
    stringified_nums = ['1', '2', '3', '4', '5000']
    assert while_condition(stringified_nums) == 4


def test_radix_sort():
    """Test with simple list."""
    from radixsort import radixsort
    nums = [5, 3, 2, 7, 9, 4, 0, 1]
    assert radixsort(nums) == [0, 1, 2, 3, 4, 5, 7, 9]


def test_radix_sort_verbose():
    """Test with many lists."""
    from radixsort import radixsort
    # test on 100 lists
    for i in range(100):
        # generate random length of list
        list_length = random.randint(0, 100)
        unsorted_list = []
        for x in range(list_length):
            # generate random numbers for random length list
            unsorted_list.append(random.randint(0, 100))

        # test that list is sorted
        assert radixsort(unsorted_list) == sorted(unsorted_list)
