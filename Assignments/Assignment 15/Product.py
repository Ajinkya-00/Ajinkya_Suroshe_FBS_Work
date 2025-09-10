class Product:

    def __init__(self,pid = 101, pname = "Mobile", price = 20000, quantity = 100):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity
        print("Constructor is called.")
    
    def showProduct(self):
        print("Product ID :",self.id)
        print("Product Name :",self.name)
        print("Price :",self.price)
        print("Quantity :",self.quantity)
    
    def __del__(self):
        print("Destructor is called.")

p1 = Product(102, "Laptop", 40000, 50)
p1.showProduct()
del p1

print("################")

p2 = Product()
p2.showProduct()

