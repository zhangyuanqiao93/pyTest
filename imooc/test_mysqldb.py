# 2017/6/2 by Bridge
import pymysql

# connect mysql database
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='tkkj')
cur = conn.cursor()
cur.execute('select * from pytest')

for r in cur.fetchall():
    print(r)

cur.close()  # close cursor object
conn.close()  # close connect


#############################
# cur.fetchone()  # 返回结果集的下一行
# cur.fetchmany()  # 返回结果集的下几行
# cur.fetchall()  # 返回结果集的所有行
# cur.rowcount()   # 返回最后一次execute返回数据的行数或影响行数

cur.rownumber  # 相当于指针


