from abc import ABC, abstractmethod

class Vehicles(ABC):

    def __init__(self, wheels, person):
        self.wheels = wheels
        self.person = person

    @abstractmethod
    def calSal(self):
        return 0

class TwoWheels(Vehicles):
    def calSal(self):
        toll = 20
        if(self.person > 2):
            toll += (self.person - 2) * 10
        return toll
    
class ThreeWheels(Vehicles):
    def calSal(self):
        toll = 30
        if(self.person > 3):
            toll += (self.person - 3) * 20
        return toll
    
class FourWheels(Vehicles):
    def calSal(self):
        toll = 40
        if(self.person > 4):
            toll += (self.person - 4) * 40
        return toll
    
class HeavyVehicles(Vehicles):
    def calSal(self):
        toll = 60
        if(self.person > 6):
            toll +=(self.person - 6) * 100
        return toll





print("TOLL CALCULATION SYSTEM\n")

wheels = int(input("Enter number of wheels: "))
persons = int(input("Enter number of persons: "))

if wheels == 2:
    v = TwoWheels(wheels, persons)
elif wheels == 3:
    v = ThreeWheels(wheels, persons)
elif wheels == 4:
    v = FourWheels(wheels, persons)
elif wheels > 4:
    v = HeavyVehicles(wheels, persons)
else:
    print("Invalid vehicle type!")

print(f"\nTotal Toll to be paid: {v.calSal()}")