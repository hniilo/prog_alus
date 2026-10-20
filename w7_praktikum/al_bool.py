
# Leia arvud mis jaguvad 3 VÕI 5ga. for tsükliga käin elemendid läbi
def jada(nums):
    arvude_list = []
    for el in nums:
        if el % 3 == 0 or el % 5 == 0:
            arvude_list.append(el)
    return sum(arvude_list)
            

# Näide, kuidas kasutada lambda funktsiooni ja järjendi koostajat (list-comprehensionit).
# Esmalt deklareerime lambda funktsiooni, mis võtab argumendi nums.
# Tavaline for tsükkel kõikide nums elementide kohta: for el in nums.
# sum ja for vahel on element - sellele rakendatakse tingimust if järel: el % 3 == 0 or el % 5 == 0.
# Peale for tsüklit ja tingimuste täitmist tagastatakse sum() sulgude sisse tingimustele
# vastav järjend (list).
# sum(list) arvutab ja tagastab tingimusega filtreeritud listi elementide summa
# lambda funktsioon tagastab filtreeritud listi elementide summa.
jada_lambda = lambda nums: sum([el for el in nums if el % 3 == 0 or el % 5 == 0])


numbers = range(1000)

# kutsutakse for-loopi kasutav funktsioon
print(jada(numbers))
# kasutatakse lambda funktsiooni sama tulemuse saamiseks
print(jada_lambda(numbers))