def half_pyramid_hardcoded_lines_right(symbol):
    """Write right side of pyramid as ASCII graphics"""
    print("half_pyramid_hardcoded_lines_right:")
    for i in range(1, 7):
        print(symbol * i)


half_pyramid_hardcoded_lines_right('t')

def half_pyramid_dynamic_lines_left(height):
    """Write left side of pyramid as ASCII graphics"""
    print("half_pyramid_dynamic_lines_left:")
    for i in range(height):
        spaces = " " * (height - i)
        stars = "*" * (i + 1)
        print(spaces, stars)


half_pyramid_dynamic_lines_left(7)


def pyramid_dynamic_lines_symbols(height, symbol):
    print("pyramid_dynamic_lines_symbols:")
    for i in range(height):
        spaces = " " * (height - i)
        print(spaces, symbol * (i * 2 + 1))


pyramid_dynamic_lines_symbols(7, "#")


def pyramid_dynamic_lines_symbols(line_count, symbol):
    print("pyramid_dynamic_lines_symbols, without additional variable declaration:")
    for i in range(line_count):
        print((line_count - i) * " " + (i * 2 + 1) * symbol)


pyramid_dynamic_lines_symbols(5, "+")
