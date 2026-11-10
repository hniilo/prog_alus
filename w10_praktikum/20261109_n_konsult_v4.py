'''
As an introduction to sorting lists in
Python you'll have to implement two functions.

In this exercise we represent students as a
pair of (mark, full_name), so a tuple of two elements.

And in this exercises we represent students as
lists of pairs, like:
>>> students = [
    (85, "Susan"),
    (6, "Joshua"),
    (37, "Jeanette")
]

sudent_grades = [85, 6, 37]

Part 1
Write a function named sort_by_mark
that take as argument a list of students
and returns a copy of it sorted by mark
in descending order.
Such as:

>>> sort_by_mark(students)
[(85, "Susan"), (37, "Jeanette"), (6, "Joshua")]

'''
def sort_by_mark(students):
    return sorted(students, reverse = True)

def sort_by_name(students):
    return sorted(students,
                  key = lambda student: student[1])


students = [
    (85, "Susan"),
    (6, "Joshua"),
    (37, "Jeanette")
]
print(sort_by_mark(students))
print(sort_by_name(students))



def sorted(lst, key, reverse):
    pass


