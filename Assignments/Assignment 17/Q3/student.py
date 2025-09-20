class Student:
    def __init__(self, student_id=0, name="", age=0, percentage=0.0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Pass"