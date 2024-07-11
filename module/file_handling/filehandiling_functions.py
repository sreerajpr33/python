# f=open('python/module/file_handling/new1.txt','x')
# f.write('abcdefghijk'+'lmnopqrstuvwxyz')

# f=open('python/module/file_handling/new4.txt','w')
# f.write('welcome')

# f=open("module/file_handling/new2.txt","w")
# r=int(input('enter the limit'))
# for i in range(r):
#     name=input('enter the names :')
#     f.write(name)

# f=open("python/module/file_handling/new2.txt","a")
# r=int(input('enter the limit'))
# for i in range(r):
#     name=input('enter the names :')
#     f.write(name)

# f=open("python/module/file_handling/new2.txt","r")
# print(f.read())

# f=open("python/module/file_handling/new2.txt","r")
# print(f.read(3))
# print('_'*5)

# f=open("python/module/file_handling/new2.txt","r")
# print(f.readline(2))
# print('_'*5)
# print(f.readline(4))

# f=open("python/module/file_handling/new2.txt","r")
# print(f.readlines())

# f=open("python/module/file_handling/new2.txt","r")
# l=len(f.readlines())
# f.seek(0)
# for i in range(l):
#     a=f.readline().strip()
#     print(a[::-1])

# f=open("python/module/file_handling/new2.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# let=0
# cap=0
# for i in range(l):
#     a=f.readline().strip()
    
#     for j in a:
#         if j==' ':    #printing words
#             word+=1
        
#         else:
#             let+=1    #printing words

#             if j.isupper():   
#                 cap+=1         #printing capitalletters

#     print(a[::1])
#     word+=1
# print(word)
# print(let)
# print(cap)
# print(let-cap)    #printing samallletters

            
import os
# os.remove()
# os.mkdir('sk')
# os.rmdir('sk')
print(os.path.exists('d'))
    


