class Square:
    side = 3
    def __init__(self, x):
        self.side = x


    def area(self):
        return self.side*self.side

sq  = Square(4)
print(Square.side)
print(Square.area(sq))
#or
print(sq.area())