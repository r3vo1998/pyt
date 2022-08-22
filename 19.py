class Triangle():
    def __init__(self, f, s, t):
        self.first = f
        self.sec = s
        self.third = t
        
    def area(self):
        return (self.first + self.sec + self.third) / 2

triangle = Triangle(25, 63, 47)
print(triangle.area())
