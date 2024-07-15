class A:
    def a1(self):
        print('a1')
class B:
    def b1(self):
        print('b1')
class F:
    def f1(self):
        print('f1')
class C(A,B):
    def c1(self):
        print('c1')
class D(B,F):
    def d1(self):
        print('d1')
class E(C,D):
    def e1(self):
        print('e1')

sr=A()
sr.a1()

hh=B()
hh.b1()

ii=F()
ii.f1()

E=E()
E.f1()