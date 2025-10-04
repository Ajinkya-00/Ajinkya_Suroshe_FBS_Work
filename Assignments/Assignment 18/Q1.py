class CompleNumber:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
        print("Constructor is called.")

    def __del__(self):
        print("Destructor is called.")

    def __add__(self, other):
        return CompleNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return CompleNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f'{self.real} + {self.imag}'
    
c1 = CompleNumber(3, 4)
c2 = CompleNumber(1, 2)

print("Addition :", c1 + c2)
print("Subtraction :", c1 - c2)