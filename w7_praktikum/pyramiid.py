def pyramid_reverse(korgus, symbol):
    pyr_asc = []
    for i in range(korgus):
        pyr_asc.append((korgus - i - 1) * " " + (i * 2 + 1) * symbol + (korgus - i - 1) * " ")
        # Kasutan listi objektile kohalduvat funktsiooni reversed()
    for el in reversed(pyr_asc):
        print(el)


def create_pyramid_rows(lines_count, symbol):
    """returns list of strings. Elements are ASCII graphics elements for pyramid"""
    pyr = []
    for i in range(lines_count):
        pyr.append((lines_count - i - 1) * " " + (i * 2 + 1) * symbol + (lines_count - i - 1) * " ")
    return pyr


pyr_asc = create_pyramid_rows(7, '*')
pyr_len = len(pyr_asc)
for el in range(pyr_len):
    print(pyr_asc[el] + "|" + pyr_asc[-el - 1] + "|" + pyr_asc[el])


def create_pyramid_rows_comprehension(lines_count, symbol):
    """Oneliner example - to complicated for production"""
    return [(lines_count - row - 1) * " " + (row * 2 + 1) * symbol + (lines_count - row - 1) * " " for row in range(lines_count)]


for line in create_pyramid_rows_comprehension(5, "@"):
    print(line)
