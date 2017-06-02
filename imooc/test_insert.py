# 2017/6/2 by Bridge
import pymysql

# connect mysql database
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='tkkj')
cur = conn.cursor()


# select_sql = 'select * from pytest'
insert_sql = 'insert into pytest VALUES (NULL ,"xx",12)'
update_sql = 'update pytest set name = "BB" WHERE id = 2'
delete_sql = 'delete from tkkj.pytest WHERE id < 3'

# 数据回滚

try:
    cur.execute(insert_sql)
    print(cur.rowcount)
    cur.execute(update_sql)
    print(cur.rowcount)
    # mysql 自动关闭数据的事务处理
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()



cur.execute(delete_sql)
print(cur.rowcount)

# cur.execute(select_sql)
# rs = cur.fetchall()

# for rs in cur.fetchall():
#     print(rs)

# 对获取的数据进行操作
# for row in rs:
# print('id = %s,username = %s,age = %s' % row)




#############################
# cur.fetchone()  # 返回结果集的下一行
# cur.fetchmany()  # 返回结果集的下几行
# cur.fetchall()  # 返回结果集的所有行
# cur.rowcount()   # 返回最后一次execute返回数据的行数或影响行数

# cur.rownumber  # 相当于指针

cur.close()  # close cursor object
conn.close()  # close connect
