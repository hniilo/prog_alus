
def print_maatriks(matrix):
    for el in matrix:
        print(el)

def print_peadiagonaal(matrix):
    suurus = len(matrix)
    for el in range(suurus):
        #print(el, suurus - el - 1)
        #print(matrix[el][- el - 1])
        print(matrix[el][suurus - el - 1])

maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print_maatriks(maatriks)
# print_peadiagonaal(maatriks)


# Kuidas kätte saada listi elemendid "ringis"
def prindi_ringiga_jaak(loend, algus):
    n = len(loend)
    for samm in range(n):
        indeks = (algus + samm) % n
        print(loend[indeks])

def prindi_ringiga_uus_list(loend, algus):
    for element in loend[algus:] + loend[:algus]:
        print(element)

puuviljad = ["õun", "pirn", "banaan", "kiivi", "mango"]
prindi_ringiga_jaak(puuviljad, 2)
print()
prindi_ringiga_uus_list(puuviljad, 2)
