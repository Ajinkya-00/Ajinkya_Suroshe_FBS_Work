class Student:
    def __init__(self, student_id = 0, name = "", age = 0, per = 0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.per = per
    
    def claculateRank(self):
        if self.per >= 75:
            return "Distinction"
        elif self.per >= 60:
            return "First Class"
        elif self.per >= 50:
            return "Second Class"
        else:
            return "Pass"
