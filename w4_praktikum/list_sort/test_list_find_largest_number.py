import pytest

from list_find_largest_number import second_largest


def test_second_largest_basic():
    assert second_largest([10, 40, 30, 20, 50]) == 40


def test_second_largest_unsorted():
    assert second_largest([25, 143, 89, 13, 105]) == 105


def test_second_largest_descending():
    assert second_largest([54, 23, 11, 17, 10]) == 23


def test_second_largest_with_duplicates():
    assert second_largest([5, 5, 3, 1]) == 5


def test_second_largest_two_elements():
    assert second_largest([1, 2]) == 1


def test_second_largest_negative_numbers():
    assert second_largest([-1, -5, -3]) == -3


def test_second_largest_single_element_raises():
    with pytest.raises(IndexError):
        second_largest([7])
