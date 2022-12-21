import sqlite3

conn = sqlite3.connect('C:\db\mydb.db')

print("Opened database successfully")
studentdet = conn.execute("select * from STUDENTDETAIL")

#print(studentdet.fetchall())

for i in studentdet.fetchall():
    print(i)

