class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
    
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        m = m + cm // 100
        cm = cm % 100
        km = km + m // 1000
        m = m % 1000

        return Distance(km, m, cm)
    
    def __sub__(self, other):
        total1 = self.km*100000 + self.m*100 + self.cm
        total2 = other.km*100000 + other.m*100 + other.cm

        diff = abs(total1 - total2)

        km = diff // 100000
        diff = diff % 100000
        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)
    
    def __str__(self):
        return f'{self.km} km {self.m} m {self.cm} cm'
    
d1 = Distance(2, 750, 80)
d2 = Distance(1, 500, 50)

print("Addition :", d1 + d2)
print("Subtraction :", d1 - d2)