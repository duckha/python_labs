class Square:
    def __init__(self, side):
        self.side = side

    def getP(self):
        return self.side * 4

    def getS(self):
        return self.side ** 2


s = Square(5)
s1 = Square(10)
print("hello")
print(s.getP())
print(s1.getP())
print(s1.getS())
