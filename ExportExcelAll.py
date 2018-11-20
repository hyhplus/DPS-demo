#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import xlwt                                 # excel文件模块
import time


def export(table_name, files, search_sql):

    db = pymysql.connect('localhost', 'root', '123456', 'dps_demo', charset='utf8')
    cursor = db.cursor()                    # 获取游标

    cursor.execute(search_sql)              # 执行SQL

    cursor.close()                          # 游标关闭
    db.close()                              # 连接关闭

    # files = [file[0] for file in cursor.description]
    all_data = cursor.fetchall()            # 所有数据
    print(all_data)

    book = xlwt.Workbook(encoding='utf-8')  # 先创建一个 book
    sheet = book.add_sheet('sheet1')        # 在创建一个 sheet

    for col, file in enumerate(files):      # 写表头
        sheet.write(0, col, file)

    # row = 1
    # for data in all_data:                 # 写数据(数据表的记录)，不能写时间格式
    #     for col, file in enumerate(str(data)):
    #         sheet.write(row, col, file)
    #     row += 1

    for row in range(1, len(all_data)+1):
        for col in range(0, len(files)):    # 写数据(数据表的记录)
            # 这里必须使用str(), 否则时间格式无法识别
            text = str(all_data[row-1][col])

            if text == 'None':
                text = ' '
            sheet.write(row, col, text)

    # 记录导出表格时间，区别表格，防止旧表格被新表格覆盖
    time1 = time.time()
    print(time1)
    current_time = time.strftime('%Y-%m-%d#%H.%M.%S', time.localtime(time.time()))
    print(current_time)

    book.save('D:/%s_%s.xls' % (table_name, current_time))  # 保存为excel文件


if __name__ == '__main__':

    files_ = ['生产线名称', '工位',  '产线状态', '停线时刻', '停线时间（秒）', '停线次数']
    searchSQL = 'select pName, workNumber, status, stopTime, timeCount, stopCount from line_stop;'
    export('生产线停线状况', files_, searchSQL)

    files_1 = ['生产线名称', '工位No', '停线时刻', '停线时间（秒）']
    searchSQL1 = 'select pName, workNumber, stopTime, timeCount from line_stop where status like "%延迟%" '
    export('作业状况', files_1, searchSQL1)
