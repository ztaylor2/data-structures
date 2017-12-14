"""Quicksort."""


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

if __name__ == '__main__':
    unsorted_list = [6, 6, 4, 8, 9, 3, 0, 1, 5]
    print(quicksort(unsorted_list))
