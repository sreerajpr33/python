import sqlite3
con=sqlite3.connect("python\database\employe\employe1.db")
def add():
    name =str(input('ENTER THE NAME :'))
    age =int(input('ENTER THE AGE :'))
    exp=int(input('EXPERIANCE :'))
    position=input('ENTER THE POSITION :')
    salary=int(input('ENTER THE SALARY :'))
    con.execute("insert into employe(name,age,experiance,position,salary)values(?,?,?,?,?)",(name,age,exp,position,salary))
    con.commit()
def update():
    oldname=str(input('ENTER THE OLD NAME :'))
    data=con.execute("select * from employe where name=?",(oldname,))
    f=0
    for i in data:
        newname=str(input('ENTER NEW NAME'))
        newage=int(input('enter new age :'))
        newexp=int(input('enter your experiance :'))
        newpos=input('enter new position :')
        newsal=input('enter new salary :')
        con.execute("update employe set name=?,age=?,experiance=?,position=?,salary=? where name=? ",(newname,newage,newexp,newpos,newsal,oldname))
        con.commit()
        f=1
    if f==0:
        print('name not found')
def delete():
    dname=str(input('ENTER NAME TO DELETE :'))
    data=con.execute("select * from employe where name=?",(dname,))
    f=0
    for i in data:
        con.execute("delete from employe where name= ?",(dname,))
        con.commit()
        f=1
    if f==0:
        print('name not found')
def display():
    data=con.execute("select * from employe")
    print(data)


    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format('name','age','experiance','position','salary'))
    print('_'*75)
    for i in data:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4]))
def search():
    
    sname=str(input('search the name :'))
    data=con.execute("select * from employe where name=?",(sname,))
    f=0
    for i in data:
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format('name','age','experiance','position','salary'))
            print('_'*75)
            print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4]))
            f=1
    if f==0:
        print('invalid')