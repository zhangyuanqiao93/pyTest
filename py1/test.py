# print('100+300')


# 以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。
# 其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
a = 100
if a > 0:
    print(a)
else:
    print(-a)

# //十六进制的123
b = 0x123

# 字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
print('I\'m \"OK\"!')

# Python允许用'''...'''的格式表示多行内容
# Python还允许用r''表示''内部的字符串默认不转义
print('''line1
line2
line3''')

print(10 // 3)  # 地板除//，即两个整数相除还是整数
print(10 % 3)
print(True and False)

c = 19
if c > 18:
    print('adult')
else:
    print('child')

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('我'))
print(ord('想'))
print(ord('你'))

print(chr(25105))
print(chr(24819))
print(chr(20320))

# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')  # 两种写法完全是等价的

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。


# 区分'ABC'和b'ABC',前者是str ，后者是一个字节一个字节的
x = b'ABC'  # python 对bytes类型的数据用带有b前缀的单引号或者双引号标识

# Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示


# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))

print(len('abc'))
print(len('中文'))

# 在utf-8 编码下，一个中文字符占3个字节，而1个英文字符只占用1个字节
print(len('中文'.encode('utf-8')))


# 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# /usr/bin/env/python3

# 指定编码格式为utf-8，按照UTF-8编码读取源代码
# -*- coding: utf-8 -*-



# Python格式化
# 常见的问题是如何输出格式化的字符串。
# 我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，
# 而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式
# 用%解决

print('Hello, %s' % ("World"),'今天吃%s'%('冒菜'))

print('尊敬的%s'% ("VIP"),'用户','您当月%s'%('话费'),'剩余量不足，请及时充值')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hi,%s,Nice Shoes,$%d.' % ('Curry',10000))


# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('%2d-%02d'% (3,1))
print('%.2f'%(3.14159))


