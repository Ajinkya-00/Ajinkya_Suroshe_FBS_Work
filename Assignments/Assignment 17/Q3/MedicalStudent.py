from student import Student

class MedicalStudent(Student):
    def __init__(self, student_id=0, name="", age=0, percentage=0.0, specialization="", internship_marks=0.0):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.internship_marks = internship_marks

    def accept(self):
        self.student_id = int(input("Enter Student ID : "))
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.percentage = float(input("Enter Percentage : "))
        self.specialization = input("Enter Specialization : ")
        self.internship_marks = float(input("Enter Internship Marks : "))
    
    def display(self):
        print("ID :",self.student_id)
        print("Name :",self.student_id)
        print("Age :",self.student_id)
        print("Percentage :",self.student_id)
        print("Specialization :",self.specialization)
        print("Internship Marks :",self.internship_marks)
    
    def calculateRank(self):
        total = (self.percentage + self.internship_marks) / 2
        if total >= 85:
            return "Outstanding"
        elif total >= 65:
            return "Very Good"
        else:
            return "Satisfactory"
        
m1 = MedicalStudent()
print("===========================")
m1.accept()
print("===========================")
m1.display()
print("Rank :",m1.calculateRank())
print("===========================")
print(m1)
