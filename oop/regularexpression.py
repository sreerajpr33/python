# a='wElcome'
import re
# print(re.sub('w','W',a))

# print(re.split('e',a))
# print(re.split('e',a,1))

# print(re.sub('w','W',a))

# print(re.search('w',a))

# if re.search('[a-z]',a):
#     print('a-z used')
#     if re.search('[1-9]',a):
#         print('numbers used')
#     else:
#         print('add numbers!')
# else:
#     print('no')
# a='abcd'
# print(re.search('a...',a))
# print(re.search('b.*',a))
# print(re.search('c.+',a))
# print(re.search('b.?',a))

# print(re.search('[A-Z].*',a))
# print(re.search('[a-z].?',a))
# print(re.search('[a-z].+',a))
# print(re.search('[a-z]..',a))
# print(re.search('[a-z].',a))


# a='Abcd123'
# print(re.search('[a-b]',a))                      
# print(re.search('[A-Z].*[a-z][0-9]',a))     #AND
# print('[A-Za-z1-9]',a)                      #OR
# print('[3$]',a)                             #$



# a=''
# a=str(input('enter phno :'))
# if len(a)==10 and a.isdigit():
#     if re.search('[6-9].{9}',a):
#         print('valid phone no!')                #phone no validation
#     else:
#         print('invalid phno!')
# else:
#     print("invalid")



a=input('enter email :')
if re.search('[A-Za-z1-9].*@gmail.com',a):
    print('valid')
else:
    print('invalid')
