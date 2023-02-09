class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return "x is - {} \ny is - {}".format(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y
        return ""
    
    def dist(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2)**(1/2)
        print((self.x - x)**2)
        print((self.y - y)**2)
        return round(dist, 3)


p = Point(3, 5)
print(p.move(2, 4))
print(p.show())
print(p.dist(3, 5))