vahemik = range(3, 100000000, 3)

# print(vahemik)

# for el in vahemik:
#     print(el)

# print("järjendi loomine:")
# jarjend = [el for el in vahemik if el % 21 == 0]
# print(jarjend, type(jarjend))


gen = (el for el in vahemik if el % 21 == 0)
print(gen, type(gen))

for el in gen:
    #siin saan teha
    print("gen", el)
    #siin saan teha