#素数列表
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisiable(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    num = _odd_iter()
    while True:
        n = next(num)
        num = filter(_not_divisiable(n), num)
        yield n

#生成器有连续的返回值，所以可以用for循环来遍历，若primes()函数没有连续的返回值，则for循环是有限次
for n in primes():
    if n < 10:
        print(n)
    else:
        break
# g = primes()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in primes():
#     print(primes())
#     if (i < 10):
#         print(i)