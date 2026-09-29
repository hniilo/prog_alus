def summa(a, b):
    return a + b


def lahutamine(a, b):
    return a - b


def korrutamine(a, b):
    return a * b


def jagamine(a, b):
    return a / b

def taisarvuline_jagamine(z, y):
    return z // y


operaatorid = {
    "+": summa,
    "-": lahutamine,
    "/": jagamine,
    "*": korrutamine,
    "//" : taisarvuline_jagamine
}
