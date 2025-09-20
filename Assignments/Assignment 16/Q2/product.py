class Product:

    discount = 0

    def __init__(self,pid = 0, pname = "", price = 0, quantity = 0):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity
          
    def showProduct(self):
        print("Product ID :",self.id)
        print("Product Name :",self.name)
        print("Price After Discount :",self.price)
        print("Quantity :",self.quantity)
    
    def applydiscount(self):
        if Product.discount > 0:
            self.price = self.price - (self.price * Product.discount / 100)
    
    def __del__(self):
        print("Destructor is called.")

p1 = Product(102, "Laptop", 100000, 50)
Product.discount = 10
p1.applydiscount()
p1.showProduct()