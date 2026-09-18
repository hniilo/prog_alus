'''
Create a function that takes a list of numbers and returns the second largest number.
'''

def second_largest_sorted(lst):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]

def second_largest_sort(lst):
    lst.sort(reverse=True)
    return lst[1]



def second_largest_manual_sort(lst):
    largest = float('-inf')
    second_largest = float('-inf')
    for number in lst:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest