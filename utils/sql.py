#!/usr/bin/python3
# -*- coding: utf-8 -*-


create_sql = """
CREATE TABLE product_line_stop(
    pName int, 
    productPlan varchar(200), 
    theoreticalYield int,
    realNumber int,
    status varchar(20), 
    stopTime date, 
    all_stopTime int, 
    stop_count int
)default charset=utf8;
"""


create_employee_sql = """
CREATE TABLE EMPLOYEE (
     FIRST_NAME  CHAR(20) NOT NULL,
     LAST_NAME  CHAR(20),
     AGE INT,  
     SEX CHAR(1),
     INCOME FLOAT )"""


drop_exit_line = 'DROP TABLE IF EXISTS line_stop'


create_table_line_stop = """
CREATE TABLE line_stop(
    pName varchar(20),
    workNumber varchar(20),
    productPlan varchar(100),
    theoryNumber float  NULL,
    realNumber float ,
    status varchar(20) ,
    stopTime time  NULL,
    timeCount int  NULL,
    allTimeCount int  NULL,
    stopCount int  NULL
)default charset=utf8;"""


insert_line = """
INSERT INTO line_stop(pName, workNumber, status, stopTime) values('H1', 'NO1', '延迟', '15:25:10');
"""
