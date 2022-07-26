class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Marcus", "CyberSecurity", 5, True)
print(student2.name)
#########  class = defines student | Object = Student (age, major, gpa)  #########
