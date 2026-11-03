a = "asd"
b = 5
c = 1.6
d = [1, 2, 3, 4, 5, 6]
e = [1, 2, 3, "2jaak", (6, 3, 4), [4, 3, 2, 1], {"jaak": "paak", "sam": "grill"}]
s = {1, 1, 2, 3, 4, 4}
t = (1, 1, 2, 3, 4, 4,)

case = 5

muutujate_list = [a, b, c, d, e, s, t, "Lomp On Loll - Vennaskond"]

def capitalize(algne_string):
    return algne_string.upper()

# String tüüpi muutuja prindi uppercase'ina
for element in muutujate_list:
    if isinstance(element, str):
        print("str:", capitalize(element))
        
    if isinstance(element, int):
        print("int:", element)
        
    if isinstance(element, float):
        print("float:", element)
        
    if isinstance(element, list):
        print("list:", element)
        
    if isinstance(element, tuple):
        print("tuple:", element)
        
    if isinstance(element, dict):
        print("dict:", element)
        
    if isinstance(element, set):
        print("set:", element)


