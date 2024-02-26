# shape -> ractangle -> square
# square = jafnar hliðar
# rectangle = ekki jafnar hliðar

# perimeter = 2(l+w)
# area = w*l

from shape import Shape

class Rectangle(Shape):
    def __init__(self, length_x, length_y):
        self.length_x = length_x
        self.length_y = length_y

    def get_area(self):
        return self.length_x * self.length_y

    def get_perimeter(self):
        return 2*(self.length_x + self.length_y)

r = Rectangle(2, 4)
print(r)