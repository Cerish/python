print('hello world')
print('100+200=', 100+200)

def product(*args):
    if(len(args) <= 0):
        print('参数不能为空')
        # raise TypeError('参数列表不能为空')
    else:
        sum = 1
        for x in args:
            sum = sum * x
        return sum
print(product())

def findMinAndMax(L):
    if(len(L) == 0):
        return (None, None)
    else:
        min,max = L[0],L[0]
        for num in L:
            if(num < min):
                min = num
            if(num > max):
                max = num
        return (min, max)
print(findMinAndMax([1,10,50,-3,-10,100]))

#修改不正规的字符为---首字母大写，其他字母小写
def normalize(name):
    def f(x):
        return x[:1].upper() + x[1:].lower()
    return map(f, name)

print(list(normalize(['adam', 'LISA', 'barT'])))

#接受一个List 并利用 reduce求积
from functools import reduce
def prod(L):
    def product(x, y):
        print(x * y)
        return x * y
    return reduce(product, [3,5,7,9])
print('3*5*7*9=', prod([3,5,7,9]))

#字符型转化为浮点型
def str2float(str):
    print(type(str))
str2float('123.456')