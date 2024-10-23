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

class E(B,C,D) :
    def m5(self):
        print("This is class E")

obj_E=E()

obj_E.m1()
obj_E.m2()
obj_E.m3()
obj_E.m4()
obj_E.m5()