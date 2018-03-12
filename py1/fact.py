# 函数的递归调用
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))
print(fact(5))


# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
# **********   解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的  *************

def facter(n):
    return facter_item(n, 1)


def facter_item(num, product):
    if num == 1:
        return product
    return facter_item(num - 1, num * product)
    # 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


# 所以说一共就三步
# 把 n-1 号盘子移动到缓冲区
# 把1号从起点移到终点
# 然后把缓冲区的n-1号盘子也移到终点
def move(n, fro, buffer, to):
    if n == 1:
        print('Move', n, 'Fro', fro, 'To', to)
    else:
        move(n-1, fro, to, buffer)
        move(1, fro, buffer, to)
        move(n-1, buffer, fro, to)
