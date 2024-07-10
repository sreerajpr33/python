# f=open('python/module/file_handling/new1.txt','x')
# f.write('abcdefghijk'+'lmnopqrstuvwxyz')

# f=open('python/module/file_handling/new4.txt','w')
# f.write('welcome')

f=open("module/file_handling/new2.txt","w")
r=int(input('enter the limit'))
for i in range(r):
    name=input('enter the names :')
    f.write(name)

