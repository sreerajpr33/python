'''year=int(input('enter years of service :'))
if year>5:
    salary=int(input('enter current salary :'))
    print('your new salary is :',salary*0.05+salary)
else:
    print('no bonus were added')    

a=int(input('enter a number :'))
last_digit=a%10
if last_digit %3==0:
    print("the last digit is divisible by 3")
else:
    print("last number is not divisible by 3")

day=int(input("enter a number from 1 and 7 :"))
if day==1:
    print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("invalid number")

city=str(input("select a city(delhi,agra,jaipur :)"))
if city==("delhi"):
   print("monument of city is red fort")
elif city==("agra"):
   print("monument of city is taj mahal")if city=("delhi"):
   print("monument is red fort")
elif city==("jaipur"):
   print("monument of city is jai mahal")
else:
   print("invalid city")
   
unit=int(input("enter the unit :"))
if unit<=100:
    print("no charge")
elif unit<=200:
    unit-=100
    print('5rs may increase as per unit,current charge is :',unit*5)
else:
    print('10rs may increase as per unit,current charge is',(unit-200)*10+500)'''

for i in range(1,11):
     print(i)

for i in range(1,10,2):
     print(i)


  