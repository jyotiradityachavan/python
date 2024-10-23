class A :
    def m1(self) :
        print("class A's m1 method")

    def m2(self) :
        print("class A's m2 method")

    def m3(self) :
        print("class A's m3 method")

class B :

    def m1(self) :
        print("class B's m1 method")

    def m2(self) :
        print("class B's m2 method")

    def m3(self) :
        print("class B's m3 method")


obj_A=A()
obj_B=B()

for Capital in (obj_A,obj_B) :
    Capital.m1()
    Capital.m2()
    Capital.m3()