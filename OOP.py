import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    
Vector1 = Vector2D(1,2)
Vector2 = Vector2D(3,4)
print(Vector1 + Vector2)