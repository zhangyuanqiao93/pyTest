# -*- coding:utf-8 -*-
import sys
import pymysql


class TramsferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enogh_money(source_acctid, money)
            self.reduce_moeny(source_acctid,money)
            self.add_money(target_acctid, money)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        raise e

    def check_acct_available(self, acctid):
        cursor = conn.cursor()
        try:
            sql = "select * from account WHERE acctid= %s" % acctid
            cursor.execute(sql)
            print("check_acct_available" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s不存在' % acctid)
        finally:
            conn.close()  # 在此过程中出现问题，关闭掉连接



    def has_enogh_money(self, acctid, money):
        cursor = conn.cursor()
        try:
            sql = "select * from account WHERE acctid= %s AND  money > %s" % (acctid,money)
            cursor.execute(sql)
            print("has_enogh_money" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s余额不足' % acctid)
        finally:
            conn.close()  # 在此过程中出现问题，关闭掉连接

    def reduce_moeny(self,acctid, money):
        cursor = conn.cursor()
        try:
            sql = "update account set money = money - %s WHERE acctid = %s" % (money, acctid)
            cursor.execute(sql)
            print("reduce_moeny" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s扣款失败' % acctid)
        finally:
            conn.close()  # 在此过程中出现问题，关闭掉连接

    def add_money(self, acctid, money):
        cursor = conn.cursor()
        try:
            sql = "update account set money = money + %s WHERE acctid = %s" % (money, acctid)
            cursor.execute(sql)
            print("add_money" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s加款失败' % acctid)
        finally:
            conn.close()  # 在此过程中出现问题，关闭掉连接


if __name__ == "__main__":

    # source_acctid = sys.argv[1]  # 付款方
    source_acctid = float(input("付款账号： "))
    # input(source_acctid)
    # target_acctid = sys.argv[2]  # 收款方
    target_acctid = float(input("收款账号： "))
    # input(target_acctid)
    # money = sys.argv[3]  # 转账金额
    money = float(input("转账金额： "))
    # input(money)

    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', port='3306', db='tkkj')
    tr_money = TramsferMoney(conn)
    # 转账操作
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print('出现问题：' + str(e))
    finally:
        conn.close()
