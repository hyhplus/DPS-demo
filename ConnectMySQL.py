#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from utils import sql

# MySQL数据库连接
db = pymysql.connect('localhost', 'root', '123456', 'dps_demo', charset='utf8')

# 获取游标
cursor = db.cursor()

# 事务处理
try:
    cursor.execute(sql.drop_exit_line)
    cursor.execute(sql.create_table_line_stop)
    cursor.execute(sql.insert_line)
except Exception as e:
    db.rollback()   # 事务回滚
    print('事务处理失败', e)
else:
    db.commit()     # 事务提交

# cursor.execute(sql.create_employee_sql)

cursor.close()      # 游标关闭
db.close()          # 连接关闭

