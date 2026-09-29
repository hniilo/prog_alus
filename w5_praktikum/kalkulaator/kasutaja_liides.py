import funktsioonid

x = int(input("sisesta esimene arv: "))
y = int(input("sisesta teine arv: "))
tehe = input("sisesta tehte tüüp: ")

print(funktsioonid.operaatorid[tehe](x, y))
