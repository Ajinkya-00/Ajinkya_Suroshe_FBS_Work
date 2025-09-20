from student import Student

class College(Student):
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students
        self.students = []
    
    def addStudent(self):
        if len(self.students) < self.no_of_students:
            s = Student(101, "Ajinkya")
            s.accept()
            self.students.append(s)
            print("Student added successfully.")
        else:
            print("College is full!")
    
    def getStudent(self, student_id): 
        for s in self.students:
            if s.student_id == student_id:
                print("Student found.",s)
                return
            print("Student Not Found.")
    
    def removeStudent(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student removed.")
                return
            print("Student not found.")
        
n = int(input("Enter number of students allowed in college : "))
c = College(n)

while True:
    print("\n1. Add Student\n2. Get Student\n3. Remove Student\n4. Show All\n5. Exit")
    choice = int(input("Enter choice : "))

    if choice == 1:
        c.addStudent()
    elif choice == 2:
        sid = int(input("Enter Student ID to search : "))
        c.getStudent(sid)
    elif choice == 3:
        sid = int(input("Enter Student ID to remove : "))
        c.removeStudent(sid)
    elif choice == 4:
        print(c)
    elif choice == 5:
        break
    else:
        print("Invalid choice.")