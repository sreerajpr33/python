from add import *
from display import *
from upd import*
from delet import*
data=[]
while True:
    print("1.add \n2.display\n3.update\n4.delete\n5.exit")
    ch=int(input('enter your choice :'))
    if ch==1:
        add(data)  
    elif ch==2:
        display(data)
    elif ch==3:
        upd(data)
    elif ch == 4:
        delet(data)
    elif ch == 5:
        print("You had exited")
        break
    else:
        ("Invalid input")




