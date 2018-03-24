class Square:
    side = 0

    def area(self):
        return self.side*self.side

sqr1  = Square()

sqr1.side =  5
area = sqr1.area()
print(area)