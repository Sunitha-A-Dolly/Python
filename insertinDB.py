import sqlite3

conn = sqlite3.connect('C:\db\mydb.db')

print("Opened database successfully")

conn.execute("INSERT INTO STUDENTDETAIL (ID,NAME,AGE,ADDRESS) \
      VALUES (2, 'Paul', 12, 'California' )")

conn.commit()

print("Table inserted successfully")

conn.close()