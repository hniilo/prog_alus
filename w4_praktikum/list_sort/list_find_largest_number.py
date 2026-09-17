'''
Create a function that takes a list of numbers and returns the second largest number.
'''

def second_largest(lst):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[1]
    lst.sort(reverse=True)
    return lst[1]

print(second_largest([10, 40, 30, 20, 50]))
print(second_largest([25, 143, 89, 13, 105]))
print(second_largest([54, 23, 11, 17, 10]))