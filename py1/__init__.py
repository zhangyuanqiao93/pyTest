print('Hello');



# list数组,数组长度len(classmates) - 1
classmates = ['Mike','Bob','Curry']
print(len(classmates))

# 直接获取最后一个元素classmates[-1]
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
print(classmates[-1])   # 数组越界


# 元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'Jack')
print(classmates)

# .pop()默认删除list最后一个元素，也可以指定pop(i)
classmates.pop()
print(classmates)

classmates.insert(1,'Jack')
print(classmates)

# 替换某元素
classmates[1] = 'Sarah'
print(classmates)

# 可以包含不同类型的元素
L = ['Bob',123,True]
print(L)

# 数组可以为空，长度为0
lis = []


# q[0][1] 相当于二维数组
p=['asp','php']
q=[p,'python','java','C#']
print(p[0])
print(q[0][1])

# tuple：另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
name_list = ['Jack', 'Mike', 'Chris', 1]
print(name_list)

name_tuple = ('Jack','Mike','Chris')
print(name_tuple)

# Python规定:要定义一个只有1个元素的tuple，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

# 可以在tuple内部包含list
tuple_test = ('java','php','python',['C','C#'])
print(tuple_test)





