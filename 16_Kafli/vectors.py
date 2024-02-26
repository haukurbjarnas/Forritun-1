import math

TOLERANCE = 0.000_000_1


class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
            return f"[[ {self.x} {self.y} {self.z} ]]"
            

    def __abs__(self) -> float:
        sum = float(math.sqrt(self.x**2 + self.y**2 + self.z**2))
        return sum

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: "Vector") -> bool:
        if abs(self - other) < TOLERANCE:
            return True
        else:
            return False

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return Vector(scalar * self.x, scalar * self.y, scalar * self.z)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __gt__(self, other: "Vector") -> bool:
        return bool(abs(self) > abs(other))

    def __ge__(self, other: "Vector") -> bool:
        return bool(abs(self) >= abs(other))

    def __lt__(self, other: "Vector") -> bool:
        return bool(abs(self) < abs(other))

    def __le__(self, other: "Vector") -> bool:
        return bool(abs(self) <= abs(other))
    
    def dot(self, other: "Vector") -> float:
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other: "Vector") -> "Vector":
        return Vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)