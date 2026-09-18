import pytest

import list_find_largest_number as lfln


NUMBER_CASES = [
    ([10, 40, 30, 20, 50], 40),
    ([25, 143, 89, 13, 105], 105),
    ([54, 23, 11, 17, 10], 23),
    ([5, 5, 3, 1], 5),
    ([1, 2], 1),
    ([-1, -5, -3], -3),
]


@pytest.mark.parametrize("list_data, expected", NUMBER_CASES)
def test_second_largest_sorted(list_data, expected):
    assert lfln.second_largest_sorted(list_data) == expected


def test_second_largest_sorted_single_element_raises():
    with pytest.raises(IndexError):
        lfln.second_largest_sorted([7])


@pytest.mark.parametrize("list_data, expected", NUMBER_CASES)
def test_second_largest_sort(list_data, expected):
    assert lfln.second_largest_sort(list(list_data)) == expected


def test_second_largest_sort_single_element_raises():
    with pytest.raises(IndexError):
        lfln.second_largest_sort([7])



@pytest.mark.parametrize("list_data, expected", NUMBER_CASES)
def test_second_largest_manual_sort(list_data, expected):
    assert lfln.second_largest_manual_sort(list_data) == expected
