# def _odd_iter():
#     n = 11
#     while True:
#         n = n + 1
#         yield n

# def _not_divisiable(n):
#     return lambda x : x == int(str(n)[::-1])

# def palindrome():
#     yield 11
#     num = _odd_iter()
#     while True:
#         m = next(num)
#         yield m
#         num = filter(_not_divisiable(n), num)

# for n in palindrome():
#     if n < 1000:
#         print(n)
#     else:
#         break
def is_palinderome(s):
    ii=str(s)
    # for n in range(0,len(ii)):
    #     print(ii[n])
    #     if ii[n]!=ii[::-1]:
    #         break
    if (ii[0:] != ii[::-1]):
        return 
    return s

print(list(filter(is_palinderome,range(100))))