def summa(a, b):
    return a + b

def lahutamine(a, b):
    return a - b

def korrutamine(a, b):
    return a * b

def jagamine(a, b):
    return a / b

x = int(input("sisesta esimene arv: "))
y = int(input("sisesta teine arv: "))
tehe = input("sisesta tehte tüüp: ")

operaatorid = {
    "+" : summa(x, y),
    "-" : lahutamine(x, y),
    "/" : jagamine(x, y),
    "*" : korrutamine(x, y),
    }

print(operaatorid[tehe])