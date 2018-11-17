#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import xlwt                                 # excel文件模块
# import datetime


def export(table_name, files):

    db = pymysql.connect('localhost', 'root', '123456', 'dps_demo', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from %s;' % table_name  # sql可以考虑写进参数
    cursor.execute(sql)

    # files = [file[0] for file in cursor.description]
    all_data = cursor.fetchall()            # 所有数据
    print(all_data)

    book = xlwt.Workbook(encoding='utf-8')  # 先创建一个 book
    sheet = book.add_sheet('sheet1')        # 在创建一个 sheet

    for col, file in enumerate(files):      # 写表头
        sheet.write(0, col, file)

    # row = 1
    # for data in all_data:                 # 写数据(数据表的记录)
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

    book.save('files/%s2.xls' % table_name)  # 保存为excel文件


if __name__ == '__main__':

    files_ = ['生产线名称', '工位', '生产计划', '理论产量', '实际产量', '产线状态',
              '停线时刻', '停线时间（秒）', '总停线时间（秒）', '停线次数']
    export('line_stop', files_)
