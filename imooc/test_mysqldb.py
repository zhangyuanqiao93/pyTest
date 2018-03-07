# 2017/6/2 by Bridge
import pymysql

# connect mysql database
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='tkkj')
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='tkkj')
cur = conn.cursor()
cur.execute('select * from python_test')
# cur.execute('select * from pytest')

for r in cur.fetchall():
    print(r)

print('已经连接本地数据库')
cur.close()  # close cursor object
conn.close()  # close connect

#############################
# cur.fetchone()  # 返回结果集的下一行
# cur.fetchmany()  # 返回结果集的下几行
# cur.fetchall()  # 返回结果集的所有行
# cur.rowcount()   # 返回最后一次execute返回数据的行数或影响行数

# cur.rownumber  # 相当于指针

print('Hello World')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 计算提成了多少百分点

score1 = 72
score2 = 85
r = score2 - score1

print('成绩提升了 {0:.1f}%'.format(r / score1 * 100))
print(r / score1)

#  list实例
classmates = ['Tom', 'Bob', 'Marry']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])  # 获取最后一个元素，注意元素末位的索引是len-1，因为是从0开始计数
print(classmates[-1])  # 获取最后一个原始，用-1作索引

classmates.append('James')  # 在末尾追加一个元素
print(classmates)

classmates.insert(1, 'Tony')  # 将元素插入到指定位置
print(classmates)

classmates.pop()  # 删除末尾元素，pop()不指定默认为-1
print(classmates)
classmates.pop(1)  # 删除指定位置的元素，即第二个元素
print(classmates)

classmates[0] = 'Sam'  # 把某个元素替换成别的元素
print(classmates)

#  tuple元组
t = ();
print(t)

t = (1,)  # 定义只有一个元素的元组时，必须要加,来消除歧义。
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

print(L[-1])

# input 带有条件的判断

# s = input('birth: ')
# birth = int(s)  # 将str类型转换成int类型
# if birth >= 2000:
#     print('00后')
# else:
#     print('00前')

weight = 48
height = 1.63

BMI = weight / (height * height)

if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环遍历
names = ['Tom', 'Jane', 'Marry']
for name in names:
    print(name)

sum = 0
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range()表示生成0-(X-1)的整数序列
print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

n = 0
while n <= 100:
    print(n)
    if n > 10:
        break  # break可以提前结束循环
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # 用continue语句跳过某些循环
    print(n)
print('END')

# dict 相当于map
d = {'Marry': 95, 'Tom': 90}
print(d['Marry'])

print('Marry' in d)  # 通过in判断是否存在key
s = d.get('Tom', -1)
print(s)
print(d.get('Tomas'))  # None
print(d.get('Tomas'), -1)  # None

print(d.pop('Tom'))
print(d)

# set  也是一组key的集合，但是不存储value。由于key不能重复，所以在key中没有重复的key，
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s3 = set([2, 3, 4])
print(s1 & s3)
print(s1 | s3)

n1 = 255
n2 = 1000
print(str(n1) + ' 十六进制:' + hex(n1), str(n2) + ' 十六进制:' + hex(n2))
print(str(n1) + ' 十六进制数：' + hex(n1), str(n2) + ' 十六进制数：' + hex(n2))


# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):  # 如果不是int 或者是float
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    if x < 0:
        return -x


print(my_abs(-99))


# 定义一个空函数
def nop():
    pass  # 什么都不做，用作占位符


# 定义一个函数返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 返回的是一个tuple


# 函数的参数（位置参数）
def power(x, n):
    sum = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# 默认参数（n=2）
def power1(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power1(5))  # None


def enroll(name, gender, age=6, city='Beijing'):
    print("name: ", name)
    print("gender: ", gender)


print(enroll('Mr.Zhang', 'M'))


# 可变参数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end([1, 2, 2]))


# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。


# 可变参数
# 以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


# 定义可变参数,在函数参数前加一个*号
def calc1(*numbers):
    sum1 = 0
    for number in numbers:
        sum1 = sum1 + number * number
    return sum1


print(calc1(1, 2, 3))
nums = [2,3,4]
print(calc1(nums[0],nums[1],nums[2]))
print(calc1(*nums))