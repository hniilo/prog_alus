'''
1.1. Leida ühest suurem täisarv, mille ruut võrdub selle arvu kümnendnumbrite
summa (ristsumma) kuubiga.
'''

#n1, n1^2 == RS^3
def ristsumma(arv:int)-> int:
    rs = 0
    for el in (str(arv)):
        rs = rs + int(el)
    return rs

i = 1
while(True):
    i += 1
    if i**2 == ristsumma(i)**3:
        print(i)
        break
