# tagasta esimesed 10 astme ruutu
ruudud = []

for el in range(5, 9):
    ruudud.append(el**2)
        
#print(ruudud)
print(len(ruudud))
print("esimene", ruudud[:10])


# Näide for tsükli continue ja break kohta
ruudud_teine = []
loendur = 0
for el in range(5, 100):
    ruudud_teine.append(el**2)
    loendur = loendur + 1
    # kui loendur on väiksem kui 9, jätka, muidu välju tsüklist
    if loendur <= 9:
        continue
    else:
        break
    
    
print(ruudud_teine)
print("teine", len(ruudud_teine))


# Sama mis eelmine näide, lihtsalt tingimus on teine ja kasutusel ainult break
ruudud_kolmas= []
loendur = 0
for el in range(5, 7):
    ruudud_kolmas.append(el**2)
    loendur = loendur + 1
    # kui loendur on väiksem kui 9, jätka, muidu välju tsüklist
    if loendur > 9:
        break
        
print(ruudud_kolmas)
print("kolmas", len(ruudud_kolmas))

