#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('C:\db\mydb.db')

print("Opened database successfully")
sqlquery = '''CREATE TABLE STUDENTDETAIL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50) );'''

conn.execute(sqlquery)
print("Table created successfully")

conn.close()