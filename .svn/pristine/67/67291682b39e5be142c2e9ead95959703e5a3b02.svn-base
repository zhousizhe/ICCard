import pymysql
import sqlite3
from UI import cacheUtil, xmlUtil


def conn_excu_sql(sql):
    loginType = cacheUtil.getCache("loginType")
    if int(loginType) == 0:
        host = xmlUtil.getValue("DataBase", "ip", "value")
        user = xmlUtil.getValue("DataBase", "user", "value")
        passwd = xmlUtil.getValue("DataBase", "passwd", "value")
        db = xmlUtil.getValue("DataBase", "db", "value")
        conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    elif int(loginType) == 1:
        conn = sqlite3.connect('./topcharge.db')
        # conn = sqlite3.connect('.\\topcharge.db')
    else:
        return
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur, conn