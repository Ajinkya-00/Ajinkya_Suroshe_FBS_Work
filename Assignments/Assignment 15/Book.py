class Book:

    def __init__(self,bid = 101, bname = "The Hobbit", price = 499, author = "J.R.R.Tolkien" ):
        self.id = bid
        self.name = bname
        self.price = price
        self.author = author
    
        print("Constructor is called.")
    
    
    def showBook(self):
        print("Book ID :",self.id)
        print("Book Name :",self.name)
        print("Price :",self.price)
        print("Author :",self.author)

    def __del__(self):
        print("Destructor is called")
    

b1 = Book(102, "The Eyes", 1000, "Robert")
b1.showBook()
del b1

print("################")


b2 = Book()
b2.showBook()
