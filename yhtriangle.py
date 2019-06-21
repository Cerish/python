import re
def yhtriangle(n):
    # d = {'int': "整数",'float': "浮点", 'str': "字符串", 'list': "元组", 'dict': "字典", 'set': "集合"}
    # typen = str(type(n))
    # print(typen[8:-2:1])
    # print(d[typen[8:-2:1]])
    # return
    # if isinstance(n, int) and n > 0:
        L = [1]
        print (L)
        while len(L) < int(n):
            L = [L[i]+L[i+1] for i in range(len(L)-1)]
            L.insert(0,1)
            L.append(1)
            print(L)
    # return ('参数必须为正整数')
yhtriangle(10)
