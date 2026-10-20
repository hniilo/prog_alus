# tee 6 realine pool-puu
def kool(tärn):
    for i in range(1,7):
        print(tärn*i)
    
#print(kool('t'))




def kool2(height):
    for i in range(height):
        spaces = " " * (height - i)
        stars = "*" * (i + 1)
        print(spaces, stars)
#kool2(7)


def kool3(height, sumbol):
    for i in range(height):
        spaces = " " * (height - i)
        print(spaces, sumbol * (i * 2 - 1))
#kool3(3, "#")
        
        
        
def kool4(korgus, sumbol):
    for i in range(korgus):
        print((korgus - i)* " " + (i * 2 -1) * sumbol)
kool4(5,"+")


def kool5(korgus, sumbol):
    for i in range(korgus):
        print((korgus - i)* " " + (i * 2 + 1) * sumbol)
kool5(5,"+")
    