"""Radix sort."""
from collections import OrderedDict
from que_ import Queue


def stringify_nums(nums_list):
    """."""
    stringified_nums = []
    for num in nums_list:
        stringified_nums.append(str(num))
    return stringified_nums


def while_condition(string_unsorted_list):
    """."""
    num_lengths = []
    for num in string_unsorted_list:
        num_lengths.append(len(num))
    return max(num_lengths)


def unravel_buckets(bucket_dict):
    """."""
    unraveled_nums = []
    for bucket in bucket_dict:
        while bucket_dict[bucket].peek():
            unraveled_nums.append(bucket_dict[bucket].dequeue())
    return unraveled_nums


def push_into_buckets(stringified_nums, i, buckets_dict):
    """."""
    for num in stringified_nums:
        try:
            buckets_dict[num[-i]].enqueue(num)
        except IndexError:
            buckets_dict['none'].enqueue(num)
    return buckets_dict


def radixsort(unsorted_list):
    """."""
    if len(unsorted_list) == 0:
        return unsorted_list

    stringified_nums = stringify_nums(unsorted_list)
    while_condition_int = while_condition(stringified_nums)

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

    i = 0

    while i <= while_condition_int:
        buckets_dict = push_into_buckets(stringified_nums, i, buckets_dict)
        stringified_nums = unravel_buckets(buckets_dict)
        i += 1

    numified_nums = [int(x) for x in stringified_nums]
    return numified_nums
