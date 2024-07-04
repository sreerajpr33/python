def add(a,b):
    return a+b

def sub(a,b):
    return a-b
    
mul=lambda a,b:a*b
   

div=lambda a,b:a/b
    

def numbers():   
    a=int(input('enter a number :'))
    b=int(input('enter another number :'))
    return a,b

while True:
    print('1.add\n2.sub\n3.mul\n4.div')
    choice=int(input('enter your choice :'))

    if choice==1:
        a,b=numbers()
        print(add(a,b))
    elif choice==2:
        a,b=numbers()
        print(sub(a,b))
    elif choice==3:
        a,b=numbers()
        print(mul(a,b))
    elif choice==4:
        a,b=numbers()
        print(div(a,b))
    else:
        print('invalid choice')