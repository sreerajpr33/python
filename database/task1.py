import sqlite3

con=sqlite3.connect("task1.db")

try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
con.execute("insert into student(age,name,mark)values(20,'pushpa',1)")
con.commit()