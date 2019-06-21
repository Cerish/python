print('hello world1')
# print absolute value of an integer:
a = 100
if a == 0:
  print(a)
else:
  print(-a)

print('\\\t\\')
print(r'\\\\t\\')
print('''hello,
world''')

# s = input('birth:')
# birth = int(s)
# if birth > 2000:
#     print ('00前')
# else:
#     print('00后')

sum = 0
for x in range(101):
    sum = sum + x
    sum = sum + 10
print(sum)
sum = sum + 10
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("你好，", x)

n = len(L)
while n > 0:
    print("你好，", L[n-1])
    n = n - 1

d = { 'name': 'lihua'}
print(d.get('name1'))