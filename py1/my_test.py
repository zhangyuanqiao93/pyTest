def fun(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

# fun(2)
print(fun(2))
print(fun(3,[3,2,1]))
print(fun(3))


# import datetime
# datetime.datetime.now = lambda : datetime.datetime.time(2018, 3, 8)