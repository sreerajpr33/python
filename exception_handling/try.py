# while True:
#     try:
#         a=int(input('ENTER A NUMBER:'))
#         print(a)
#         break
#     except:
#         print('enter a number!')


# l=[1,2,3,4.5,'abc',10]
# sum=0
# for i in l:
#     try:
#         sum+=i
#     except:
#         pass
# print(sum)

try:
    print('10'+'a')
except NameError:
    print('name error')
except TypeError:
    print('type error')
else:
    print('else')
finally:
    print('finally')


