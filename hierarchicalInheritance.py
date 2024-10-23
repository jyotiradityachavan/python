class A :

    def m1(self):
        print("This is class A")

class B(A) :
    def m2(self):
        print("This is class B")

class C(A) :
    def m3(self):
        print("This is class C")


class D(A) :
    def m4(self):
        print("This is class D")

class E(A) :
    def m5(self):
        print("This is class E")

obj_B=B()
obj_B.m1()
obj_B.m2()

obj_C=C()
obj_C.m1()
obj_C.m3()

obj_D=D()
obj_D.m1()
obj_D.m4()

obj_E=E()
obj_E.m1()
obj_E.m5()

