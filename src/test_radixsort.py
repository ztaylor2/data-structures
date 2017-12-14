"""Test radix sort."""

import random
from collections import OrderedDict
from que_ import Queue


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


def test_unravel_buckets():
    """."""
    from radixsort import unravel_buckets
    buckets_dict = OrderedDict({
        'none': Queue(),
        '0': Queue(),
        '1': Queue(),
        '2': Queue(),
        '3': Queue(),
        '4': Queue(),
        '5': Queue(),
        '6': Queue(),
        '7': Queue(),
        '8': Queue(),
        '9': Queue(),
    })

    for bucket in buckets_dict:
        buckets_dict[bucket].enqueue(bucket)

    assert unravel_buckets(buckets_dict) == ['none', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def test_push_into_buckets():
    """."""
    from radixsort import push_into_buckets

    buckets_dict = OrderedDict({
        'none': Queue(),
        '0': Queue(),
        '1': Queue(),
        '2': Queue(),
        '3': Queue(),
        '4': Queue(),
        '5': Queue(),
        '6': Queue(),
        '7': Queue(),
        '8': Queue(),
        '9': Queue(),
    })

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    full_buckets_dict = push_into_buckets(nums, 0, buckets_dict)

    for key in full_buckets_dict:
        if full_buckets_dict[key].peek():
            assert full_buckets_dict[key].dequeue() == key


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
