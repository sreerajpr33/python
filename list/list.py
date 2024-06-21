'''L=[1,2,'welcome',1.5,1,2]
print(L[2])
if 2 in L:
    print()
else:
    print()
for i in L:
    print(i)
print(type(L))
print(len(L))
L[2]=['hello ']
print(L)
del L[3]
print(L)'''

'''L=[30,20,'welcome']
L.append(20)
print(L)
L.insert(2,45)
print(L)
L.extend([100,200])
print(L)
L.remove('welcome')
print(L)
L.pop(1)
print(L)
L.clear()'''

L=[10,10,1,'abc']
print(L.index(1))
print(L.count(10))
B=L.copy()
print(B)

B.pop()
print(B)
print(L)

L=[12,3,45,3]
L.sort()
print(L)
L.reverse()
print(L)

