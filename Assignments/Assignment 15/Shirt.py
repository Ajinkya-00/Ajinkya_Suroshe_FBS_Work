class Shirt:

    def __init__(self, sid = 100, sname = "Rymond", type = "Formal", price = 1500, size = "S/M/L"):
        self.id = sid
        self.name = sname
        self.type = type
        self.price = price
        self.size = size
        print("Constructor is called.")
    
    def showShirt(self):
        print("Shirt ID :",self.id)
        print("Name :",self.name)
        print("Type :",self.type)
        print("Price :",self.price)
        print("Size :",self.size)
      
    def __del__(self):
        print("Destructor is called.")

s1 = Shirt(101, "Peter England", "Cotton", 2000, "S/M/L")
s1.showShirt()

del s1
print("#######################")

s2 = Shirt()
s2.showShirt()