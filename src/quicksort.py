"""Quicksort."""

import random
import timeit


def quicksort(unsorted_list):
    """Sort a unsorted_list."""
    if len(unsorted_list) == 0:
        return []
    if len(unsorted_list) == 1:
        return unsorted_list

    pivot = unsorted_list[0]
    left = []
    right = []
    equal = []

    for item in unsorted_list:
        if item == pivot:
            equal.append(item)
        if item < pivot:
            left.append(item)
        if item > pivot:
            right.append(item)

    return quicksort(left) + equal + quicksort(right)


def _wrapper(func, *args, **kwargs): # pragma: no cover
    def _wrapped(): # pragema: no cover
        return func(*args, **kwargs)
    return _wrapped

if __name__ == '__main__':
    unsorted_list = []
    for i in range(10):
        unsorted_list.append(random.randint(0, 1000))

    quicksort_list = _wrapper(quicksort, unsorted_list)
    print('Time to sort 1M times:')
    print(timeit.timeit(quicksort_list))
