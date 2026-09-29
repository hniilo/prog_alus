x = int(input("sisesta esimest arvu"))
y = int(input("sisesta teist arvu"))
tehe = input("sisesta tehtetüüb")

print(x, tehe, y)

if tehe == "+":
    print(x + y)
if tehe == "-":
    print(x - y)
if tehe == "*":
    print(x * y)
if tehe == "/":
    print(x / y)
else:
    print("invalid tehe")

def

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


for operator in ["+", "-", "*", "/"]:
    if tehe == operator:
        print()