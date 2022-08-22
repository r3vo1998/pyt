class Square(Shape):
    def __init__(self, l):
        self.length = l
    def calculate_perimeter(self):
        return self.length * 4
    def change_size(self, l):
        self.length = l
    
class Rectangle(Shape):
    def __init__(self, f, s):
        self.first = f
        self.sec = s
    def calculate_perimeter(self):
        return 2 * (self.first + self.sec)
