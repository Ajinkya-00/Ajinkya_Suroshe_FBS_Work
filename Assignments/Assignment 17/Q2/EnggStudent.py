from student import Student

class EnggStudent(Student):
    def __init__(self, student_id = 0, name = "", age = 0, per = 0.0, branch = "", internal_marks = 0):
        super().__init__(student_id, name, age, per)
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        self.student_id = int(input("Enter the ID : "))
        self.name = input("Enter the Name : ")
        self.age = int(input("Enter the Age : "))
        self.per = float(input("Enter the Percentage : "))
        self.branch = input("Enter the Branch : ")
        self.internal_marks = float(input("Enter Internal Marks : "))

    def display(self):
        print("ID :",self.student_id)
        print("Name :",self.student_id)
        print("Age :",self.student_id)
        print("Percentage :",self.student_id)
        print("Branch :",self.student_id)
        print("Internal Marks :",self.student_id)

    def calculateRank(self):
        total = (self.per + self.internal_marks) / 2

        if total >= 80:
            return "Excellent"
        elif total >= 60:
            return "Good"
        else:
            return "Average"

e1 = EnggStudent()
print("===========================")
e1.accept()
print("===========================")
e1.display()
print("Rank :",e1.calculateRank())
print("===========================")
print(e1)

   