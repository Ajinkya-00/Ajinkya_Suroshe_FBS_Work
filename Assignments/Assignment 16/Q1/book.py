class Book:
    count = 0

    def __init__(self,bid = 101, bname = "The Hobbit", price = 499, author = "J.R.R.Tolkien" ):
        Book.count += 1
        self.id = bid
        self.name = bname
        self.price = price
        self.author = author
    
          
    def showBook(self):
        print("Book ID :",self.id)
        print("Book Name :",self.name)
        print("Price :",self.price)
        print("Author :",self.author)
    
    @staticmethod
    def totalBook():
        print("Total Book : ", Book.count)
        print("#############################")

    def __del__(self):
        print("Destructor is called")
    

b1 = Book(101, "The Eyes", 1000, "Robert")
b1.showBook()

b2 = Book(102, "The Eyes", 1000, "Robert")
b2.showBook()



b1.totalBook()