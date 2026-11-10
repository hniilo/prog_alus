'''
Mis on algarv?

Algarv (inglise keeles prime number) on
naturaalarv, mis on
suurem kui 1
ja jagub ainult arvuga 1 ja iseendaga.
'''


def is_prime(kasutaja_sisend):
    arvud = []
    for arv in range(2, kasutaja_sisend + 1):
        if kasutaja_sisend % arv == 0:
             arvud.append(arv)           
    return len(arvud) == 1


print(is_prime(1))