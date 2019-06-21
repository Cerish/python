#如过需要倒序输出，可通过添加 reverse=True 实现。 -t[1]只适用于数值，利用添加负号直接改变数字的大小实现。
def by_name(t):
    return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name,reverse=True)
print(L2)

def by_score(t):
    return -t[1]
L3 = sorted(L, key=by_score)
print(L3)