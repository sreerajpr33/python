bio=set()
chem=set()
while True:
    print('1.add students to biology and chemistry\n2.view students\n3.view common students')
    c=int(input('enter your choice '))
    if c==1:
        bi=int(input('enter the limit of students in biology :'))
        for i in range(bi):
            name=str(input('enter student name :'))
            bio.add(name)
            # print(bio)

        ch=int(input('enter the limit of students in chemistry :'))
        for i in range(ch):
            name=str(input('enter the student name :'))
            chem.add(name)
            # print(chem)

    elif c==2:
        print('students in biology :',bio)
        print('students in chemistry :',chem)

    elif c==3:
        print('common students are :')
        print(bio.intersection(chem))
    
    else:
        print('invalid number')



