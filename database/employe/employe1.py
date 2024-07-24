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
    newname=str(input('ENTER NEW NAME'))
    con.execute("update employe set name=? where name=? ",(newname,oldname))
    con.commit()
def delete():
    dname=str(input('ENTER NAME TO DELETE :'))
    con.execute("delete from employe where name= ?",(dname,))
    con.commit()
def display():
    data=con.execute("select * from employe")
    print(data)


    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format('name','age','experiance','position','salary'))
    print('_'*75)
    for i in data:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4]))
def search():
    sname=str(input('search the name :'))
    con.execute("select * from employe where name=?",(sname,))

