import functools
min2 = functools.partial(min, 0)
print(min2(1, 50, 10, 3))

# max2 = functools.partial(max, 10)
# print(max2(5, 6, 7))

# for i in range(101, 201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     print(i)


for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            break
        if j == i - 1:
            print(i)
