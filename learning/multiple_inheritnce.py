class A:
    def where(self):
       print("I am from class A")

class B:
    def where(self):
        print("I am from class B")

class C(A, B):
    # def where(self):
    #     print("I am from class C")
    pass


an_instance_of_C = C()
an_instance_of_C.where()


# Method calling order
print("\nMethod calling Order:")
print(C.mro())


# Super Method
print("\nSuper Mehod:\n")

class A:
    def spam(self):
        print(1)
        
class B(A):
    def spam(self):
        print(2)
        super().spam()
        # super(B, self).spam()

B().spam()