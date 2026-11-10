'''

Create a program to find and print all numbers
from 0 to 1000 (both included),
that are divisible by 7
and whose digits sum are divisible by 3.

For instance,
1512 is divisible by 7 and the sum of all its is digits (9)
is divisible by 3.

Another example, 21 is divisible by 7,
and the sum of its digits (3) is divisible by 3.
Example If the exercise were to make the same computation
but in the range(1500, 1700),
the solution should print:
$ ./solution.py 1512 1533 1554 1575 1596 1617 1638 1659 1680


Looge programm,
mis leiab ja prindib kõik arvud
vahemikus 0 kuni 1000 (mõlemad kaasa arvatud),
mis jaguvad 7-ga
ja mille numbrite summa jagub 3-ga.


Näiteks 1512 jagub 7-ga ja kõigi selle 7-numbrite summa (9) jagub 3-ga. Teine näide: 21 jagub 7-ga ja selle numbrite summa (3) jagub 3-ga. Näide Kui ülesandes tehtaks sama arvutus, aga vahemikus (1500, 1700), peaks lahendus välja trükkima: $ ./solution.py 1512 1533 1554 1575 1596 1617 1638 1659 1680

'''

def leia_kohaliste_summa(taisarv):
    taisarv_str = str(taisarv)
    numbrite_summa = 0
    
    for el in taisarv_str:
        numbrite_summa += int(el)
    
    return numbrite_summa


def leia(vahemik):
    for i in vahemik:
        if i % 7 == 0 and leia_kohaliste_summa(i) % 3 == 0:
            print(i)
        
        
leia(range(0, 1000))
        
