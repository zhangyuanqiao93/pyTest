# 2017/6/2 by Bridge
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='tkkj')
cur = conn.cursor()
cur.execute('select * from pytest')

for r in cur.fetchall():
    print(r)
cur.close()
conn.close()

