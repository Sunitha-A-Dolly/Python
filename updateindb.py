import sqlite3

conn = sqlite3.connect('C:\db\mydb.db')
print("Opened database successfully")

conn.execute("UPDATE STUDENTDETAIL set NAME = 'Alex' where ID = 1")

conn.commit()


studentdet = conn.execute("select * from STUDENTDETAIL")

#print(studentdet.fetchall())

for i in studentdet.fetchall():
    print(i)

conn.close()

