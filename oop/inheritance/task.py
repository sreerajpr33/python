                                                # #single inheritance
# class college:
#     def clg(self):
#         print('reg')
#     def dep1(self):
#         print('computer science')
#     def dep2(self):
#         print('commerce')
#     def dep3(self):
#         print('maths')
# class students(college):
#     def stud(self):
#         print('reg')

# students=students()
# students.stud()
# students.dep1()

                                                # #multiple inheritance
# class school:
#     def cls(self):
#         print('1')
#     def cls2(self):
#         print('2')
#     def cls3(self):
#         print('3')
# class tution:
#     def sub(self):
#         print('computer')
#     def sub1(self):
#         print('english')
# class students(school,tution):
#     print('students')

# students=students()
# students.cls3()
# students.sub()
    

#                                                 #multilevel inheritance
# class industory:
#     def wk1(self):
#         self.database='mysql'
#         print('work1',self.database)
# class supervisor(industory):
#     def wk2(self):
#         print('work2')
#     def wk3(self):
#         print('work3')
# class staff(supervisor):
#     def helo(self):
#         print('work4')
# industory=industory()
# industory.wk1()

                                        #4.heirarchical
class industory:
    def work1(self):
        print('work1')
    
class suprvisor(industory):
    def work2(self):
        print('work2')
    
class staff(industory):
    def work3(self):
        print('work3')


aa=suprvisor()
aa.work1()
aa.work2()


        #5.hybrid
class a:
    def a1(self):
            print('a1')
class b:
    def b1(self):
        print('b1')
class f:
    def f1(self):
        print('f1')
class c(a,b):
    def c1(self):
        print('c1')
class d(b,f):
    def d1(self):
        print("d1")
class e(c,d):
    def e1(self):
        print('e1') 



ee=e()
ee.e1()
ee.c1()
ee.a1()
ee.b1()
ee.f1()
ee.d1()
ee.a1()




