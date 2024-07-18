                                            #runtime
# class sample:
#     def display(self):
#         print('sample class')
#     def s1(self):
#         print('sample class s1')
# class demo(sample):
#     def display(self):
#         print('demo display')
#         super().display()
#         print('start')
#     def d1(self):
#         print('demo class d1')
# obj=demo()
# obj.display()


class sample:
    def __init__(self,name,age):
        print('get set')
        print(name,age)
    def s1(self):
        print('sample class s1')
class demo(sample):
    def __init__(self,name,age):
        print(name,age)
        print('ready')
        super().__init__(name,age)
        print('GO !!!!!')
    def d1(self):
        print('demo class d1')
obj=demo('akhil',17)