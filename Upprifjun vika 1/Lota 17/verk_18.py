import math

TOLERANCE = 0.000000000001

class Vector:

    def __init__(self, x=0, y=0, z=0):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"[[{self.x} {self.y} {self.z}]]"
    
    def __abs__(self):

        sum = math.sqrt(self.x**2 + self.y**2 + self.z**2)

        return sum
    
    def __add__(self, other: "Vector"):

        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return f"[[{new_x} {new_y} {new_z}]]"
    
    def __sub__(self, other: "Vector"):

        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z

        return f"[[{new_x} {new_y} {new_z}]]"
    
    def __eq__(self, other: "Vector"):

        if self - other < TOLERANCE:
            return True
        else:
            return False
        
    

essi = Vector(12, 3, 4)

pessi = Vector(3, 5, 7)

jessi = Vector(3, 5, 7)

messi = jessi == pessi

print(messi)