import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="sreeraj",
    password="sree12345687", 
    database="mydatabase"   
)

cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS staff (emp_id INT, name VARCHAR(255), age INT, salary FLOAT, phno VARCHAR(20))")

print('\nstaff details')
emp = []
while True:
    print("1.add\n2.view\n3.search\n4.update\n5.delete\n6.exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = int(input('Enter ID: '))
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = float(input('Enter salary: '))
        phno = input('Enter phone number: ')  
        cursor.execute('insert into staff (emp_id, name, age, salary, phno) VALUES (%s, %s, %s, %s, %s)', (emp_id, name, age, salary, phno))
        con.commit()

    elif choice == 2:
        while True:
            ch=int(input('1.view all\n2. order by name\n3. norder by salary\n4.exit\nenter your choice:'))
            if ch==1:
                cursor.execute('SELECT * FROM staff')
                data = cursor.fetchall()
                print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("emp_id", "name", "age", "salary", "phno"))
                print('_' * 65)
                for i in data:
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
            elif ch==2:
                cursor.execute('SELECT * FROM staff order by name')
                data = cursor.fetchall()
                print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("emp_id", "name", "age", "salary", "phno"))
                print('_' * 65)                                                                                      #view by ascending order!
                for i in data:
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
            elif ch==3:
                cursor.execute('SELECT * FROM staff order by salary')
                data = cursor.fetchall()
                print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("emp_id", "name", "age", "salary", "phno"))
                print('_' * 65)
                for i in data:
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0], i[1], i[2], i[3], i[4]))
            elif ch==4:
                print('exiting!')
                break
            else:
                print('invalid choice!')




    elif choice == 3:
        emp_id = int(input('Enter ID: '))
        cursor.execute('SELECT * FROM staff WHERE emp_id = %s', (emp_id,))
        data = cursor.fetchall()
        if data:
            print("{:<10}{:<20}{:<10}{:<10}{:<15}".format("Emp ID", "Name", "Age", "Salary", "Phone Number"))
            print('-' * 65)
            for i in data:
                print("{:<10}{:<20}{:<10}{:<10}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('Invalid ID')

    elif choice == 4:
        emp_id = int(input('Enter ID: '))
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = float(input('Enter salary: '))
        phno = input('Enter phone number: ')
        
        cursor.execute('UPDATE staff SET name = %s, age = %s, salary = %s, phno = %s WHERE emp_id = %s', (name, age, salary, phno, emp_id))
        con.commit()

    elif choice == 5:
        emp_id = int(input('Enter ID: '))
        cursor.execute('DELETE FROM staff WHERE emp_id = %s', (emp_id,))
        con.commit()


    elif choice == 6:
        print("You are exited")
        break
    else:
        print('Invalid choice')