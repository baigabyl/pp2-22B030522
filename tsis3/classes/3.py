class Shape(object):
    def __init__(self):
        pass
        
    def area(self):
        return 0

class Ractangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.l = l
        self.w = w

    def area(self):
        return self.l*self.w

aRactangle= Ractangle(3, 5)
print (aRactangle.area())