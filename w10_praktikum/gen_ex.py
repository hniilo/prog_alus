def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# for num in count_up_to(5):
#     print(num)

print(count_up_to(5))

generaator =  (count_up_to(5))
while True:
    next(generaator)