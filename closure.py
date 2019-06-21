def count():
    fs = []
    def f(j):
        # def g():
        #     return j * j
        # return g
        return lambda: j * j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def counter():
    L = [0]
    def count():
        L[0] += 1
        return L[0]
    return count
counterA = counter()
# print(counterA)
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5


L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
print(L)

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
# print(L)