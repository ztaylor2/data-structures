"""Radix sort."""
from collections import OrderedDict
from stack import Stack


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
    return max(num_lengths) - 1


def unravel_buckets(bucket_dict):
    """."""
    unraveled_nums = []
    for bucket in bucket_dict:
        # import pdb; pdb.set_trace()
        while bucket_dict[bucket].peek():
            unraveled_nums.append(bucket_dict[bucket].pop())
    return unraveled_nums


def push_into_buckets(stringified_nums, i, buckets_dict):
    """."""
    for num in stringified_nums:
        try:
            buckets_dict[num[-i]].push(num)
        except IndexError:
            buckets_dict['none'].push(num)
    return buckets_dict


def radixsort(unsorted_list):
    """."""
    stringified_nums = stringify_nums(unsorted_list)
    while_condition_int = while_condition(stringified_nums)

    buckets_dict = OrderedDict({
        'none': Stack(),
        '0': Stack(),
        '1': Stack(),
        '2': Stack(),
        '3': Stack(),
        '4': Stack(),
        '5': Stack(),
        '6': Stack(),
        '7': Stack(),
        '8': Stack(),
        '9': Stack(),
    })

    i = 0

    while i <= while_condition_int:
        buckets_dict = push_into_buckets(stringified_nums, i, buckets_dict)
        stringified_nums = unravel_buckets(buckets_dict)
        i += 1

    numified_nums = [int(x) for x in stringified_nums]
    return numified_nums
