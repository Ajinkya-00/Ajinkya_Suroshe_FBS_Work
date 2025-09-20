class Shirt:

    size_increase = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    def __init__(self, sid = 0, sname = "Unknown", stype = "Casual", price = 0, size = "small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        self.adjustPrice()

    def __del__(self):
        print(f"Shirt object with ID {self.sid} is deleted.")

    def showShirt(self):
        print("ID :",self.sid)
        print("Name :",self.sname)
        print("Type :",self.stype)
        print("Price :",self.price)
        print("Size :",self.size)
    
    def adjustPrice(self):
        if self.size in Shirt.size_increase:
            inc__per = Shirt.size_increase[self.size]
            self.price = self.price + (self.price * inc__per / 100)
            print("################################")

s1 = Shirt(101, "Peter Englnd", "Formal", 1000, "small")
s1.showShirt()

s2 = Shirt(102, "Raymond", "Casual", 1000, "xlarge")
s2.showShirt()