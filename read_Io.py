#写入文件, 'w' 会把原先的文件删除，而 'a' 则会在末尾进行添加
with open('./read.txt', 'a') as f:
    f.write('Hello, world!')


#使用 open 打开文件，无论是否报错，都使之关闭
#要读取二进制文件，比如图片、视频等，用 'rb' 模式打开
try:
    f = open('./read.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#为了简洁代码，Python引入了with语句来自动帮我们调用close()方法
#文件读完之后还没关闭，所以为空？
with open('./read.txt', 'r') as f:
    print('--------------')
    print(f.read())
    for line in f.readlines():
        print(line.strip())
