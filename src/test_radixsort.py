"""Test radix sort."""


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
    assert while_condition(stringified_nums) == 3


# def test_unravel_buckets():
#     """."""
#     from radixsort import unravel_buckets


def test_radix_sort():
    from radixsort import radixsort
    nums = [5, 3, 2, 7, 9, 4, 0, 1]
    assert radixsort(nums) == [0, 1, 2, 3, 4, 5, 7, 9]
