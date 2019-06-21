# def debug(func):
#     print('我是装饰器')
#     def wrapper():
#         print('112233')
#         return func()
#     return wrapper
# def debug1(func):
#     print('我是装饰器1')
#     def wrapper():
#         print('332211')
#         return func()
#     return wrapper
# @debug
# @debug1
# def say_hello():
#     print('hello')
# say_hello()


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()