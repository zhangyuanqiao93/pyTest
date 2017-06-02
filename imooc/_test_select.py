# 2017/6/2 by Bridge
import pymysql

# connect mysql database
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='tkkj')
cur = conn.cursor()

sql = 'select * from pytest'
cur.execute(sql)
rs = cur.fetchall()
# print(rs)

# 对获取的数据进行操作
for row in rs:
    print('id = %s,username = %s,age = %s' % row)

# 事务：访问和更新数据库存储的一个程序执行单元。
# 具有以下特性：原子性，一致性， 隔离性， 持久性

# 1.关闭commit(自动提交)
# 2. 正常结束事务/异常结束事务


sql_insert = 'insert into pytest(id,name,age) VALUES (4,"xx",20)'
cur.execute(sql_insert)

insert = cur.fetchall()
for it in insert:
    print(it)

print('Hello')
cur.close()
cur.close()
