"""Bubblesort in python."""
import random
import timeit


def bubblesort(unsorted_list):
    """Sort unsorted list."""
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swapped = True

    return unsorted_list


def _wrapper(func, *args, **kwargs): # pragma: no cover
    def _wrapped(): # pragema: no cover
        return func(*args, **kwargs)
    return _wrapped


if __name__ == '__main__': # pragma: no cover
    print('Sorting list of 100 rand nums between 0-1000')

    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = bubblesort(unsorted_list)

    bubblesort_list = _wrapper(bubblesort, unsorted_list)
    print('Time to sort 1M times:')
    print(timeit.timeit(bubblesort_list))
