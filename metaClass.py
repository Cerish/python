#使用元类

def fn(self, name= 'world'):
    print('hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('lihua')