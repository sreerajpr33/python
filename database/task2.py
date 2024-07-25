import sqlite3
student=sqlite3.connect("task2.db")
# a=int(input('ENTER THE LIMIT :'))
# for i in range(a):
try:
        student.execute("create table marks(name text,age int,mark real)")
except:
        pass
        # name=str(input('enter the name :'))
        # age=int(input('enter the age :'))
        # mark=int(input('enter the mark :'))
        # student.execute("insert into marks(name,age,mark)values(?,?,?)",(name,age,mark))
        # student.commit()

# data=student.execute("select * from marks")
# print(data)


# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# name=str(input('ENTER THE NAME :'))
# mark=int(input('mark :'))
# data=student.execute("select * from marks where name=? and mark>?",(name,mark))
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
# print()

# old=str(input('enter the name :'))
# newname=str(input('enter the new name :'))
# student.execute("update marks set name=? where name=?",(newname,old))
# student.commit()
# data=student.execute("select * from marks")
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
# print()

# student.execute("delete from marks where name='purushu'")
# student.commit()
# data=student.execute("select * from marks")
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
# print()

# data=student.execute("select * from marks where name like 'b%'")
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#         print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
# print()

# data=student.execute("select * from marks order by name desc")  #descenting=desc,ascending=default
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
# for i in data:
#         print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
# print()


data=student.execute("select name, sum(mark) from marks group by name")  #max min count avg sum
# print("{:<15}{:<15}{:<15}".format('name','age','mark'))
# print('_'*34)
for i in data:
#         print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
        print(i)