"""INsertion sort in python."""
import random
import timeit


def insertionsort(unsorted_list):
    """Sort list."""
    for i in range(1, len(unsorted_list)):
        current_val = unsorted_list[i]

        while i > 0 and unsorted_list[i - 1] > current_val:
            unsorted_list[i] = unsorted_list[i - 1]
            i = i - 1

        unsorted_list[i] = current_val

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

    sorted_list = insertionsort(unsorted_list)

    insertionsort_list = _wrapper(insertionsort, unsorted_list)
    print('Time to sort 1M times:')
    print(timeit.timeit(insertionsort_list))
