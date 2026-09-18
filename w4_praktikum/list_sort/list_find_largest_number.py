'''
Create a function that takes a list of numbers and returns the second largest number.
'''

def second_largest_sorted(lst):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]

def second_largest_sort(lst):
    lst.sort(reverse=True)
    return lst[1]



# Sellel meetodil on loogika viga- milles see seisneb?
def second_largest_manual_sort(lst):
    last_largest = 0
    largest = 0
    for number in lst:
        if number > largest:
            last_largest = largest
            largest = number
    return last_largest