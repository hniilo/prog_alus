import string
tahestik_ascii = string.ascii_lowercase


'''
str, ascii

00
01
02
03
..
10
11
...
20
'''

def print_pairs(tahestik):
    for taht in tahestik:
        for taht_kaks in tahestik:
            print(taht + taht_kaks)


print_pairs(tahestik_ascii)

# Lisa uus funktsioon, mis väldib samade topelttähtede printimist, nt aa v zz