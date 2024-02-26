# shape -> ractangle -> square

from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length):
        self.length_x = length
        self.length_y = length