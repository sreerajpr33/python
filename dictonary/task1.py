lim=int(input('enter the limit :'))
dtl=[]
for i in range(lim):
    name=input('enter the name :')
    age=int(input('enter the age :'))
    place=input('enter yhe place :')
    dtl.append({'name':name,'age':age,'place':place})
print("{:<10}{:<6}{:<6}".format("name","age","place"))
print('_'*20)
for i in dtl:
    print("{:<10}{:<6}{:<6}".format(i['name'],i['age'],i['place']))