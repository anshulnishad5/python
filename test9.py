class shape:
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

rect = rectangle(5, 3)
circ = circle(4)
print(f"Area of rectangle: {rect.area()}")  
print(f"Area of circle: {circ.area()}")  
