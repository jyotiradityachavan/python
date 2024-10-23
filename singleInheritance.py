class A :
    def m1(self):
        print("This is class A")

class B(A) :
    def m2(self):
        print("This is class B")

obj_B=B()

obj_B.m1()
obj_B.m2()