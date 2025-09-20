class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
    
    def accept(self):
        print("ID :",self.student_id)
        print("Name :",self.name)