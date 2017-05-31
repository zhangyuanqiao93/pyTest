# -*- coding: utf-8 -*-


# if语句执行有个特点，它是从上往下判断，
# 如果在某个判断上是True，把该判断对应的语句执行后，
# 就忽略掉剩下的elif和else

age = 12
if age > 18:
    print("Your age is", age)
    print('adult')
elif age > 6:
    print("Your age is", age)
    print('teenager')
else:
    print("Your age is", age)
    print('child')

    # if <条件判断1>:
    #     <执行1>
    # elif <条件判断2>:
    #     <执行2>
    # elif <条件判断3>:
    #     <执行3>
    # else:
    #     <执行4>

x = 0
if x:
    print('True')


# int()，String转换为int
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
# 并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = float(input('身高: '))
# print(type(height))   # str
wight = float(input('体重: '))
# print(type(wight))    # str
BMI = wight/(height*height)    # str不能相除
# print(type(BMI))
print(BMI)
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


# 循环

names = ['Mike','Curry','Wade']
for name in names:
    print(name)

sum1 = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1=sum1+x
    print(sum1)

# range(100): 生成一个整数序列0-99
print(list(range(100)))

sum1=0
for y in list(range(101)):
    sum1 = sum1+y
    print(sum1)


n = 99
sum2 = 0
while n > 0:
    sum2 = sum2 + n
    n = n -2
    print(sum2)


L = ['Bart', 'Lisa', 'Adam']
for z in range(len(L)):
    # print(z), L[z]
    print("Hello,%s" % (L[z]))


# dict and set (dict:map,)
name = ['A','B','C']
scores = [80,90,100]

dic = {'A': 80, 'B': 90, 'C': 100}
dic['A']
print(dic['B'])

# 数据放入dict的方法，除了初始化时指定外，还可以通过key放入
dic['B'] = 100
print(dic['B'])

print('Tomas' in dic)

print(dic.get('Tomas', -1))