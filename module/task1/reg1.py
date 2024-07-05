from add import *
from display import *
data=[]
while True:
    print("1.add \n2.display\n3.update\n4.delete\n5.exit")
    ch=int(input('enter your choice :'))
    if ch==1:
        add(data)  
    elif ch==2:
        display(data)




