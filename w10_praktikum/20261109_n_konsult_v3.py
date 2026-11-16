'''
Mis on algarv?

Algarv (inglise keeles prime number) on
naturaalarv, mis on
suurem kui 1
ja jagub ainult arvuga 1 ja iseendaga.
'''

import time
from functools import wraps

def mes_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        algus = time.perf_counter()
        tulemus = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - algus:.4f} s")
        return tulemus
    return wrapper

@mes_time
def is_prime(kasutaja_sisend):
    if kasutaja_sisend == 1:
        return False 
        
    arvud = []
    #for arv in range(2, int(kasutaja_sisend ** 0.5) + 1):
    for arv in range(2, kasutaja_sisend // 2 + 1):
    #for arv in range(2, kasutaja_sisend + 1):

        if kasutaja_sisend % arv == 0:
             arvud.append(arv)
    return len(arvud) == 0

@mes_time
def is_prime_sqrt(kasutaja_sisend):
    if kasutaja_sisend == 1:
        return False

    arvud = []
    for arv in range(2, int(kasutaja_sisend ** 0.5) + 1):
        if kasutaja_sisend % arv == 0:
            arvud.append(arv)
    return len(arvud) == 0


print(is_prime(900000000))
print(is_prime_sqrt(900000000))

'''
ma tahan printida
funktsiooni nime
mille aega mõõtsin
'''
