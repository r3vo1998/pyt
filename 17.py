import math
pi = math.pi

class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return pi * self.radius * self.radius
    
circle = Circle()
