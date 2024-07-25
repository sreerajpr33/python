import sqlite3
from employe1 import*
con=sqlite3.connect("python\database\employe\employe1.db")

try:
    con.execute("create table employe(name text,age int,experiance real,position text,salary real)")
except:
    pass
while True:
    print('1.add\n2.update\n3.delete\n4.display\n5.search')
    ch=(int(input('enter your choice :')))
    if ch==1:
        add()
    elif ch==2:
        update()
    elif ch==3:
        delete()  
    elif ch==4:
        display()
    elif ch==5:
        search()
    else:
        print('INVALID INPUT')
        