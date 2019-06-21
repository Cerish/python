# import threading

# local_num = threading.local()


# def change_it():
#     n = local_num.num
#     if n != 0:
#         print(n)


# def run_thread(n):
#     local_num.num = n
#     change_it()


# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import re
# test = '用户输入的字符串12'
# if re.match(r'用户输入的字符串1', test):
#     print('ok')
# else:
#     print('failed')

# 深度优先 与 广度优先的例子
# class Node(object):
#     def __init__(self,sName):
#         self._lChildren = []
#         self.sName = sName
#     def __repr__(self):
#         return "<Node '{}'>".format(self.sName)
#     def append(self,*args,**kwargs):
#         self._lChildren.append(*args,**kwargs)
#     def print_all_1(self):
#         print (self)
#         for oChild in self._lChildren:
#             oChild.print_all_1()
#     def print_all_2(self):
#         def gen(o):
#             lAll = [o,]
#             while lAll:
#                 oNext = lAll.pop(0)
#                 lAll.extend(oNext._lChildren)
#                 yield oNext
#         for oNode in gen(self):
#             print (oNode)

# oRoot = Node("root")
# oChild1 = Node("child1")
# oChild2 = Node("child2")
# oChild3 = Node("child3")
# oChild4 = Node("child4")
# oChild5 = Node("child5")
# oChild6 = Node("child6")
# oChild7 = Node("child7")
# oChild8 = Node("child8")
# oChild9 = Node("child9")
# oChild10 = Node("child10")

# oRoot.append(oChild1)
# oRoot.append(oChild2)
# oRoot.append(oChild3)
# oChild1.append(oChild4)
# oChild1.append(oChild5)
# oChild2.append(oChild6)
# oChild4.append(oChild7)
# oChild3.append(oChild8)
# oChild3.append(oChild9)
# oChild6.append(oChild10)

# oRoot.print_all_1()
# oRoot.print_all_2()


# # coding:utf-8
 
import json
# from urlparse import parse_qs
from wsgiref.simple_server import make_server
 
 
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    name = params.get('name', [''])[0]
    no = params.get('no', [''])[0]
 
    # 组成一个数组，数组中只有一个字典
    dic = {'name': name, 'no': no}
 
    return [json.dumps(dic)]
 
 
if __name__ == "__main__":
    port = 5088
    httpd = make_server("0.0.0.0", port, application)
    print( "serving http on port {0}...".format(str(port)))
