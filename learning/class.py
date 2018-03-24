class A:
    pass
a = A()
class B(A):
    pass

b = B()

a.__class__
b.__class__


isinstance(a, A)
isinstance(b, B)
isinstance(b, A)
isinstance(a, B)

issubclass(A, B)
issubclass(B, A)


class Student:
    pass
muni = Student()
muni.name = 'Mohian Muni'
muni.id = 10025
muni.clas  = 11

print(muni.name)
print(muni.id)
print(muni.clas)