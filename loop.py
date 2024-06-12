'''a=int(input('enter a value :'))
b=int(input('enter another value :'))
for i in range(a,b):
    print(i)

starting_value=int(input('enter a value :'))
ending_value=int(input('enter another value :'))
sum=0
for i in range(starting_value,ending_value+1):
   sum+=i
print(sum)

a=int(input('enter a value :'))
b=int(input('enter another value :'))
sum=0
for i in range(a,b):
  if i%2==1:
   sum+=i
   print(i)
print('sum :',sum)

a=int(input('enter a value :'))
b=int(input('enter another value :'))
sum=0
evensum=0
oddsum=0
for i in range(a,b+1):
    sum+=i
    if i%2==1:
       oddsum+=i
    else:
        evensum+=i   
print('sum :',sum)
print('evensum :',evensum)
print('oddsum :',oddsum)

a=1
b=int(input('enter a number to find factorial :'))
sum=1
for i in range(a,b+1):
    sum*=i
print(sum)'''

a=1
b=int(input('enter a number :'))
sum=1
for i in range(a,11):
      print(i,'*',a,'=',i*b)

      

    






