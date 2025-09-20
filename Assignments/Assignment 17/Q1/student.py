class Student:
    def __init__(self, student_id = 101, name = "Ajinkya", age = 22, percentage = 88.80):
        self.sid = student_id
        self.nm = name
        self.age = age
        self.per = percentage
    
    def Accept(self):
        self.sid = int(input("Enter the ID : "))
        self.nm = input("Enter the Name : ")
        self.age = int(input("Enter the Age : "))
        self.per = float(input("Enter the Percentage : "))
    
    def Display(self):
        print("Student ID :",self.sid)
        print("Name :",self.nm)
        print("Age :",self.age)
        print("Percentage :",self.per)
    
    def calculateRank(self):
        if(self.per >= 70):
            return "Distinction"
        elif(self.per >= 60):
            return "First Class"
        elif(self.per >= 50):
            return "Second Class"
        else:
            return "Pass"

s1 = Student()
print("###################")

s1.Accept()
print("###################")
s1.Display()

print("Rank :",s1.calculateRank())
print(s1)
print("###################")