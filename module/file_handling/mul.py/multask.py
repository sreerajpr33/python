f = open("module/file_handling/table.txt", "w")
a = int(input("Enter the number: "))
for i in range(1, 11):
    b = str(i) + " * " + str(a) + " = " + str(i * a) + "\n"
    

a = int(input("Enter the number: "))
for i in range(1, a + 1):
    for j in range(1, 11):
        b = f"{i} * {j} = {i * j}"
        print(b)
    f.write(b) 