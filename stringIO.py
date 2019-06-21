#即使在print中执行的数据，也会改变
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.getvalue())

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        print('执行了几次')
        break
    print(s.strip())
import os
print(os.name)
print(os.environ)
print(os.path.abspath('.'))

print('----------------------------')

#创建目录，生成目录，删除目录
os.path.join(r'D:/lihuajie/python/1', 'testdir')
# os.mkdir(r'D:/lihuajie/python/1')
# os.rmdir(r'D:/lihuajie/python/1')

print([x for x in os.listdir('.') if os.path.isdir(x)])


import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)