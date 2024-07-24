import sqlite3
from employe1 import*
con=sqlite3.connect("python\database\employe\employe1.db")

try:
    con.execute("create table employe(name text,age int,experiance real,position text,salary real)")
except:
    pass
while True:
    print('1.add\n2.update\n3.delete\ndisplay\n4.search')
    ch=(int(input('enter your choice :')))
    if ch==1:
        add()
        
        