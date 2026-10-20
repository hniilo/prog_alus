#Tee funktsioon, mis tagastab int'ide listi aritmeetilise keskmise

def keskmine(taisarvude_list):
    summa = sum(taisarvude_list)
    elementide_arv = len(taisarvude_list)
    keskmine = summa/elementide_arv
    return keskmine


def keskmine_hn(lst):
    return sum(lst)/len(lst)
    
    
esimene = [0,1,2,3,4,5,6,7,8,9]

#print(keskmine(esimene))
#print(keskmine_hn(esimene))



whetting_your_appetite = """Python is an easy to learn, powerful
programming language. It has efficient high-level data structures and
a simple but effective approach to object-oriented
programming. Python’s elegant syntax and dynamic typing, together with
its interpreted nature, make it an ideal language for scripting and
rapid application development in many areas on most platforms."""

#print(len(whetting_your_appetite))




'''
Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?
'''
print("Gonna knock three times:")
for i in range(3):
    print("*knock*")
    
print("- Who's there?")