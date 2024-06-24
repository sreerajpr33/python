'''name=[]
a=int(input("enter the limit :"))
for i in range(a):
    b=str(input("enter the names"))
    name.append(b)
print(name)

name=[]
while True:
    print('1.add\n2.display\n3.update\n4.delete\n5.exit')
    choice=int(input('enter your choice :'))
    if choice==1:
        limit=int(input('enter the limit :'))
        for i in range(limit):
            b=str(input("enter the names :"))
            name.append(b)
    elif choice==2:
        for i in name:
            print(i)
    elif choice==3:
        old_name=input('enter name to update :')
        if old_name in name:
            new_name=input('new_name :')
            pos=name.index(old_name)
            name[pos]=new_name
    elif choice==4:
        old_name=input('enter name :')
        if old_name in name:
            name.remove(old_name)

Original_list=[1,2,3,4,4,3,5]
unique_list = []
for item in Original_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

sum=0
L=[1,2,3,'demo']
print(L)
for i in L:
    if type (i)==int or type (i)==float:
        sum+=i
print(sum)

L=[1,5,2,7,9]
print(L)
large=max(L)
print(large)

L=[1,5,9,0]
print(L)
L.sort()
print(L[-1])'''

    
L=[12,3,4,5,6]













        



        