'''
Create a function that takes a list of numbers and returns the second largest number.
'''

def second_largest_sorted(lst):
    """Return the second largest number from a list using ``sorted``.

    Args:
        lst: A list containing at least two numbers.

    Returns:
        The second largest number in the list.

    Raises:
        IndexError: If the list contains fewer than two elements.
    """
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]

def second_largest_sort(lst):
    """Sort a list in place and return its second largest number.

    Args:
        lst: A mutable list containing at least two numbers. The list is
            sorted in descending order by this function.

    Returns:
        The second largest number in the list.

    Raises:
        IndexError: If the list contains fewer than two elements.
    """
    lst.sort(reverse=True)
    return lst[1]



# Sellel meetodil on loogika viga- milles see seisneb?
def second_largest_manual_sort(lst):
    """Attempt to find the second largest number without sorting the list.

    Args:
        lst: A list of numbers.

    Returns:
        The value stored as the previous largest number.

    Note:
        The current algorithm does not correctly handle every input, such as
        negative numbers or a second-largest value encountered after the
        largest value.
    """
    last_largest = 0
    largest = 0
    for number in lst:
        if number > largest:
            last_largest = largest
            largest = number
    return last_largest
