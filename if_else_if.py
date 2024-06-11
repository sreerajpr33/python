'''a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
d=int(input("enter a number :"))
if a>c and a>b and a>d:
    print(a)
elif b>c and b>d and b>a:
    print(b)
elif c>b and c>d and c>a:
    print(c)
else:
    print(d)

a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
d=int(input("enter a number :"))
if a>b:
    if a>c:
        if a>d:
          print(a)
        else:
          print(d)
else:
    if b>d:
          print(b)
    else:
        if c>b:
           if c>d:
            print(c) 
        else:
            print(d)


w="make a wish"
f=str(input("enter the word to check : "))
if f in w:
    print("word available")
else:
    print("not available")

p=str(input("enter a password(5-12 characters required)"))
if len(p)>=5 and len(p)<=12:
    print('valid password')
else:
    print('invalid password')'''


for i in range(10):
    print (i)

for i in range(20):
    print ('welcome')



           