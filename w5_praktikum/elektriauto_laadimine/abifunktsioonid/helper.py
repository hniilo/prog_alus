
def genereeri_kellaaegade_sammud():
    kellaajad = []
    for h in range(24):
        for m in range (0, 45+1, 15):
            # print(f"time({h}, {m}: True),")
            kellaajad += f"{h}, {m}, True\n"
    return kellaajad

with open("kellaajad.txt", "w") as f:
    lst = genereeri_kellaaegade_sammud()
    for row in lst:
        f.write(row)