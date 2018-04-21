## Defination

class Add:
    ## Initialization
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

obj = Add(3,4)

## Access
print(obj.add())
# print obj.add()
## Garbage collection



# Object life cycle

a = 45
b = a
c = [a]


del a
b = 100
c[0] = -1
