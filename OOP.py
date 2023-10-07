import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __add__(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)
    
Vector1 = Vector2D(1,2)
Vector2 = Vector2D(3,4)
print(Vector1 + Vector2)
print(Vector2)
Vector3 = Vector3D(1,2,3)
Vector4 = Vector3D(4,5,6)
print(Vector3 + Vector4)
print(Vector4)
