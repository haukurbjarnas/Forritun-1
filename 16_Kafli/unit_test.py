from vectors import Vector

u = Vector(12, 3, 4)

v = Vector(1, 2, 3)

w = u.cross(v)

print(type(w) == Vector)

print(w)