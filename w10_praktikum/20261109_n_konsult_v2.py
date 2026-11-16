print(
    sum(
        [
            el for el in range(10)
        ]
    )
)

lst = []
for el in range(10):
    lst.append(el)
print(sum(lst))

print([el ** 2 for el in range(10)])
