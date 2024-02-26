class ComplexNumber:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            self.imag = str(self.imag)
            return "{} - {}i".format(self.real, self.imag.replace("-", ""))
        if self.imag > 0:
            "{} + {}i".format(self.real, self.imag)