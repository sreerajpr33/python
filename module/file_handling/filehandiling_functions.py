# f=open('python/module/file_handling/new1.txt','x')
# f.write('abcdefghijk'+'lmnopqrstuvwxyz')

# f=open('python/module/file_handling/new4.txt','w')
# f.write('welcome')

f=open('python/module/file_handling/new2.txt','w')
l=[]
r=int(input('enter the limit'))
for i in range(r):
    name=input('enter the names :')
    l.append(name)
print(l)

