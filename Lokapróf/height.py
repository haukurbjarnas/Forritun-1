# 1 foot = 30.48 cm

# 1 foot = 12 inches

# 1 inch = 2.54

class Height:

    def __init__(self, feet, inches) -> int:

        self.feet = feet
        self.inches = inches


    def cm(self):

        self.feet_to_cm = self.feet * 30.48

        self.inches_to_cm = self.inches * 2.54

        self.centimeters = self.feet_to_cm + self.inches_to_cm

        return self.centimeters
    
    def __add__(self, other: "Height"):

        return Height(self.feet+other.feet, self.inches+other.inches)

