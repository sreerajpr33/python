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
    age =int(input('ENTER THE AGE :'))
    exp=int(input('EXPERIANCE :'))
    position=input('ENTER THE POSITION :')
    salary=int(input('ENTER THE SALARY :'))
    


    
