import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="sreeraj",
    password="sree12345687", 
    database="mydatabase"   
)
cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS emp (emp_id INT, address text,experiance int,position text)")

# data=cursor.fetchall()
# cursor.execute("select staff.emp_id,staff.name,staff.age,staff.salary,staff.phno,emp.address,emp.experiance,emp.position from staff inner join emp on staff.emp_id=emp.emp_id")
# data=cursor.fetchall()
# for i in data:
#         print(i)
# print()

# while True:
#     print("1.add")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         emp_id = int(input('Enter ID: '))
#         address = input('Enter address: ')
#         exp = int(input('Enter exp: '))
#         position = input('Enter pos: ')
#         # phno = input('Enter phone number: ')  
#         cursor.execute('insert into emp (emp_id, address, experiance, position) VALUES (%s, %s, %s, %s)', (emp_id, address, exp, position))
#         con.commit()
    
# cursor.execute("select staff.emp_id,staff.name,staff.age,staff.salary,staff.phno,emp.address,emp.experiance,emp.position from staff left join emp on staff.emp_id=emp.emp_id")
# data=cursor.fetchall()
# for i in data:
#         print(i)
# print()

# cursor.execute("select staff.emp_id,staff.name,staff.age,staff.salary,staff.phno,emp.address,emp.experiance,emp.position from staff right join emp on staff.emp_id=emp.emp_id")
# data=cursor.fetchall()
# for i in data:
#         print(i)
# print()

# cursor.execute("select staff.emp_id,staff.name,staff.age,staff.salary,staff.phno,emp.address,emp.experiance,emp.position from staff cross join emp")
# data=cursor.fetchall()
# for i in data:
#         print(i)
# print()



