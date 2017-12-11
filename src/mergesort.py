"""Merge sort in python."""


def mergesort(unsorted_list):
    """Sort a list."""
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left_half = unsorted_list[:mid]
        right_half = unsorted_list[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i = i + 1

            else:
                unsorted_list[k] = right_half[j]
                j = j + 1

            k = k + 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j = j + 1
            k = k + 1

        return unsorted_list
